from django import forms
from .models import Brand, Mecanism, Curea, Oferta, Caracteristici
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .validators import *
from .models import Ceasuri
from .models import CustomUser

class UtilizatorInregistrareForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'telefon', 
            'adresa', 
            'oras', 
            'cod_postal', 
            'data_nasterii',
            'abonat_newsletter'
        ]
        
        widgets = {
            'data_nasterii': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'adresa': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
        
    def clean_telefon(self):
        telefon = self.cleaned_data.get('telefon')
        if not telefon:
            return telefon
            
        if not telefon.isdigit():
            raise ValidationError("Numarul de telefon trebuie sa contină doar cifre.")
            
        if len(telefon) != 10:
            raise ValidationError(f"Numarul de telefon trebuie sa aiba exact 10 cifre (ai introdus {len(telefon)}).")
            
        return telefon

    def clean_cod_postal(self):
        cod = self.cleaned_data.get('cod_postal')
        if not cod:
            return cod
            
        if not cod.isdigit():
            raise ValidationError("Codul postal trebuie sa fie numeric.")
            
        if len(cod) != 6:
            raise ValidationError("Codul poștal standard are 6 cifre.")
            
        return cod

    def clean_data_nasterii(self):
        data_nasterii = self.cleaned_data.get('data_nasterii')
        if not data_nasterii:
            return data_nasterii
            
        today = date.today()
        varsta = today.year - data_nasterii.year - ((today.month, today.day) < (data_nasterii.month, data_nasterii.day))
        
        if varsta < 18:
            raise ValidationError(f"Trebuie să aveți minim 18 ani pentru a vă înregistra. (Vârsta calculată: {varsta} ani)")
            
        return data_nasterii

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Adresa de email este obligatorie.")
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Acest email este deja asociat unui cont.")
        return email

from django.contrib.auth.forms import AuthenticationForm

class LoginFormPersonalizat(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        label="Tine-ma minte timp de o zi",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    username = forms.CharField(
        label="Nume utilizator",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Introdu userul...'
        })
    )
    password = forms.CharField(
        label="Parola",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Introdu parola...'
        })
    )
class CeasForm(forms.ModelForm):
    pret_import = forms.DecimalField(
        label="Pret de Import (RON)",
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 200'}),
        help_text="Introduceți pretul de achizitie de la furnizor (fara TVA).",
        
    )
    
    adaos = forms.IntegerField(
        label="Adaos Comercial (%)",
        required=True,
        min_value=0,
        max_value=500,
        initial=20, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 20'}),
        help_text="Procentul adaugat peste pretul de import. Ex: 20 inseamna +20%."
    )
    nume_model = forms.CharField(
        label="Denumire Model",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            validate_fara_simboluri,  
            validate_fara_cuvantul_ceas 
        ]
    )
    observatii = forms.CharField(
        label="Observatii Interne",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

        validators=[validate_fara_simboluri]
    )
    class Meta:
        model = Ceasuri
        fields = ['nume_model', 'brand', 'diametru_carcasa', 'poza']
        labels = {
            'nume_model': 'Denumire Model',
            'diametru_carcasa': 'Diametru (mm)',
            'brand': 'Producator / Brand',
            'poza': 'Imagine Produs'
        }
        widgets = {
            'nume_model': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'diametru_carcasa': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def clean_nume_model(self):
        nume = self.cleaned_data.get('nume_model')
        
        if nume: 
            if len(nume) < 3:
                raise forms.ValidationError("Denumirea este prea scurta (minim 3 caractere).")
                
        return nume

    def clean_pret_import(self):
        pret = self.cleaned_data.get('pret_import')
        
        if pret:
            if pret < 50:
                raise forms.ValidationError("Nu importam produse cu valoare mai mica de 50 RON.")
                
        return pret
    def clean_diametru_carcasa(self):
        diametru = self.cleaned_data.get('diametru_carcasa')
        
        if diametru:
            if diametru < 20 or diametru > 60:
                raise forms.ValidationError(f"Diametrul de {diametru} mm nu este realist pentru un ceas de mana (intre 20 și 60).")
        
        return diametru
    def clean(self):
        cleaned_data = super().clean()
        
        pret_import = cleaned_data.get('pret_import')
        adaos = cleaned_data.get('adaos')
        if pret_import is not None and adaos is not None:
            if pret_import < 100:
                if adaos < 50:
                    msg = f"Pentru produsele ieftine (<100 RON), adaosul minim trebuie sa fie de 50% (curent: {adaos}%). Altfel profitul este neglijabil."
                    
                    self.add_error('adaos', msg)
                    self.add_error('pret_import', "Pretul este prea mic pentru acest adaos.")

        return cleaned_data
class ContactForm(forms.Form):
    nume = forms.CharField(max_length=10, label='Nume', required=True,
        validators=[
            validate_inceput_majuscula_si_caractere, # Cerinta i
            validate_capitalizare_parti              # Cerinta j
        ]
    )
    prenume = forms.CharField(max_length=10, label='Prenume', required=False,
        validators=[
            validate_inceput_majuscula_si_caractere, # Cerinta i
            validate_capitalizare_parti              # Cerinta j
        ]
    )
    cnp = forms.CharField(label='CNP', required=False, max_length=13, min_length=13,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: 1901010...'}),
        validators=[validate_cnp_custom] # Cerintele f și g combinate
    )

    data_nasterii = forms.DateField(label='Data nașterii', required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[validate_varsta_majora] # Cerinta a
    )

    email = forms.EmailField(label='E-mail', required=True,
        validators=[validate_email_netemporar] # Cerinta h
        )
    
    confirm_email = forms.EmailField(label='Confirmare E-mail', required=True)

    OPTIUNI_MESAJ = [
        ('neselectat', 'Neselectat'),
        ('reclamatie', 'Reclamație'),
        ('intrebare', 'Întrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare'),
    ]
    tip_mesaj = forms.ChoiceField(choices=OPTIUNI_MESAJ, label='Tip mesaj', initial='neselectat',
        widget=forms.Select(attrs={'class': 'form-control'}),
        validators=[validate_tip_mesaj_selectat] # Cerinta e
    )

    subiect = forms.CharField(max_length=100, label='Subiect', required=True,
            validators=[
            validate_fara_linkuri,                  # Cerinta d
            validate_inceput_majuscula_si_caractere # Cerinta i
        ])

    minim_zile_asteptare = forms.IntegerField(
        label='Pentru review-uri/cereri minimul de zile de asteptare trebuie setat de la 4 incolo iar pentru cereri/intrebari de la 2 incolo. Maximul e 30.',
        required=True, min_value=0, max_value=30
        )

    mesaj = forms.CharField(
        label='Mesaj (va rugam sa scrieti mesajul si sa va semnati)',
        required=True,
        widget=forms.Textarea(attrs={'rows': 5}),
        validators=[
            validate_mesaj_text,   # Cerintele b și c
            validate_fara_linkuri  # Cerinta d
        ]
    )
    def clean(self):
        cleaned_data = super().clean()
        
        # Extragem datele curate pentru a le compara
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        nume = cleaned_data.get('nume')
        mesaj = cleaned_data.get('mesaj')
        tip_mesaj = cleaned_data.get('tip_mesaj')
        zile_asteptare = cleaned_data.get('minim_zile_asteptare')
        cnp = cleaned_data.get('cnp')
        data_nasterii = cleaned_data.get('data_nasterii')

        if email and confirm_email:
            if email != confirm_email:
                self.add_error('confirm_email', "Adresele de email nu coincid.")

        # b. Validare Semnatura (Ultimul cuvânt din mesaj == Nume)
        if mesaj and nume:
            cuvinte = mesaj.strip().split()
            
            if cuvinte:
                ultimul_cuvant = cuvinte[-1]
                ultimul_cuvant_curat = re.sub(r'[^\w\-]', '', ultimul_cuvant)
                if ultimul_cuvant_curat.lower() != nume.lower():
                    self.add_error('mesaj', f"Mesajul trebuie sa se termine cu semnatura dumneavoastra ({nume}).")

        # c. Validare Zile Asteptare vs Tip Mesaj
        if tip_mesaj and zile_asteptare is not None:
            # Pentru review-uri/cereri -> minim 4 zile
            if tip_mesaj in ['review', 'cerere']:
                if zile_asteptare < 4:
                    self.add_error('minim_zile_asteptare', f"Pentru o cerere de tip '{tip_mesaj}', minimul de asteptare este de 4 zile.")

            # Pentru intrebari -> minim 2 zile
            elif tip_mesaj == 'intrebare':
                if zile_asteptare < 2:
                    self.add_error('minim_zile_asteptare', "Pentru intrebări, minimul de asteptare este de 2 zile.")

        # d. Validare CNP vs Data Nasterii
        if cnp and data_nasterii:
            if len(cnp) == 13 and cnp.isdigit():
                try:
                    s = int(cnp[0])
                    aa = int(cnp[1:3])
                    ll = int(cnp[3:5])
                    zz = int(cnp[5:7])
                    prefix_an = 0
                    if s in [1, 2]: prefix_an = 1900
                    elif s in [5, 6]: prefix_an = 2000
                    an_complet = prefix_an + aa
                    data_din_cnp = date(an_complet, ll, zz)
                    if data_din_cnp != data_nasterii:
                        self.add_error('cnp', f"CNP-ul introdus nu corespunde cu data nasterii selectata ({data_nasterii}).")
                        self.add_error('data_nasterii', "Aceasta data nu corespunde cu CNP-ul introdus.")

                except ValueError:
                    self.add_error('cnp', "Data extrasa din CNP este invalida.")

        return cleaned_data
    
def validare_fara_cifre(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Acest camp nu are voie sa contina cifre!')
class FiltruCeasuriForm(forms.Form):
    # folosind validator standard
    nume_model = forms.CharField(
        required=False,
        label='Nume Model',
        widget=forms.TextInput(attrs={'placeholder': 'Minim 3 caractere...'}),
        validators=[
            MinLengthValidator(3, message="Te rugam sa introduci cel putin 3 caractere pentru cautare.")
        ]
    )

    # folosind validator custom
    tip_geam = forms.CharField(
        required=False,
        label='Tip Geam',
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Safir'}),
        validators=[validare_fara_cifre]
    )

    # folosind parametrul min_value
    pret_min = forms.DecimalField(
        required=False,
        label='Pret Min',
        min_value=10,
        error_messages={
            'min_value': 'Pretul minim trebuie sa fie de cel putin 10 RON.',
            'invalid': 'Introdu o valoare numerica valida.'
        },
        widget=forms.NumberInput(attrs={'placeholder': 'Min 10'})
    )
    
    pret_max = forms.DecimalField(
        required=False, 
        label='Preț Max', 
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Max'})
    )

    stoc_min = forms.IntegerField(required=False, label='Stoc Min', min_value=0)
    stoc_max = forms.IntegerField(required=False, label='Stoc Max', min_value=0)
    
    diametru_min = forms.IntegerField(required=False, label='Diametru Min', min_value=0)
    diametru_max = forms.IntegerField(required=False, label='Diametru Max', min_value=0)


    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        empty_label="Toate Brandurile",
        label='Brand'
    )
    mecanism = forms.ModelChoiceField(
        queryset=Mecanism.objects.all(),
        required=False,
        empty_label="Toate Mecanismele",
        label='Mecanism'
    )
    curea = forms.ModelChoiceField(
        queryset=Curea.objects.all(),
        required=False,
        empty_label="Toate Curelele",
        label='Curea'
    )
    oferta = forms.ModelChoiceField(
        queryset=Oferta.objects.all(),
        required=False,
        empty_label="Toate Ofertele",
        label='Ofertă'
    )

    # Many-to-Many
    caracteristici = forms.ModelMultipleChoiceField(
        queryset=Caracteristici.objects.all(),
        required=False,
        label='Caracteristici',
        widget=forms.CheckboxSelectMultiple
    )
    # paginare
    nr_pagini = forms.ChoiceField(
        choices=[(5, '5'), (10, '10'), (15, '15'), (20, '20')],
        label='Afisează pe pagină',
        required=False,
        initial=5,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        
        verificari = [
            ('pret_min', 'pret_max', 'Pretul'),
            ('stoc_min', 'stoc_max', 'Stocul'),
            ('diametru_min', 'diametru_max', 'Diametrul')
        ]
        
        for min_field, max_field, nume in verificari:
            min_val = cleaned_data.get(min_field)
            max_val = cleaned_data.get(max_field)
            if min_val is not None and max_val is not None and min_val > max_val:
                self.add_error(min_field, f'{nume} minim nu poate fi mai mare decat cel maxim.')
                
        return cleaned_data