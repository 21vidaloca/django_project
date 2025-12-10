import os
import json
import re
import uuid
import time
import locale
from .utils import valideaza_si_activeaza_cod
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from decimal import Decimal
from django.http import Http404
from datetime import datetime
from collections import Counter
from .clase import Accesare
from django.http import HttpResponse
from .models import Ceasuri
from .models import Brand
from django.core.paginator import Paginator
from .forms import ContactForm
from .forms import FiltruCeasuriForm
from django import forms
from django.shortcuts import render, redirect
from datetime import datetime, date
from django.conf import settings
from .forms import CeasForm
from django.contrib import messages
from .forms import UtilizatorInregistrareForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginFormPersonalizat

def index(request):
    
    return render(request, 'aplicatie/simplu.html')
try:
    locale.setlocale(locale.LC_TIME, 'ro_RO.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')
def pagina_despre(request):
    return render(request, 'aplicatie/despre.html')
def pagina_in_lucru(request):
    return render(request, 'aplicatie/in_lucru.html')
istoric_accesari=[]
def bloc_de_cod(request):
    ip_client = request.META.get('REMOTE_ADDR')
    full_url = request.get_full_path()
    istoric_accesari.append(Accesare(ip_client=ip_client, full_url=full_url))

def adaugare_produs(request):
    if request.method == 'POST':
        form = CeasForm(request.POST, request.FILES)
        
        if form.is_valid():
            produs = form.save(commit=False)
            
            pret_import = form.cleaned_data['pret_import']
            adaos = form.cleaned_data['adaos']
            # pret=Import * (1 + Adaos/100)
            factor = 1 + Decimal(adaos) / 100
            produs.pret = pret_import * factor
            
            if produs.pret > 5000:
                produs.stoc = 3
                produs.tip_geam = "Safir (Premium)"
            elif produs.pret > 1000:
                produs.stoc = 10
                produs.tip_geam = "Cristal Mineral"
            else:
                produs.stoc = 50
                produs.tip_geam = "Plastic/Acryl"

            produs.save()
            return redirect('produse')
    else:
        form = CeasForm()
    context={
        'form': form
    }
    return render(request, 'aplicatie/adaugare_produs.html', context)
def afis_data(valoare_parametru):
    
    acum = datetime.now()
    data_formatata = acum.strftime("%A, %d %B %Y").capitalize()
    ora_formatata = acum.strftime("%H:%M:%S")

    html_output = '<h2>Data si ora</h2>'
    
    if valoare_parametru == 'zi':
        html_output += f"<p>{data_formatata}</p>"
    elif valoare_parametru == 'timp':
        html_output += f"<p>{ora_formatata}</p>"
    else:
        html_output += f"<p>{data_formatata}, ora {ora_formatata}</p>"
        
    return html_output


def info(request):
    bloc_de_cod(request)
    data_html_string = None 
    if 'data' in request.GET:
        valoare_parametru = request.GET.get('data', '')
        data_html_string = afis_data(valoare_parametru)
    ip_client = request.META.get('REMOTE_ADDR')
    full_url = request.get_full_path()
    
    accesare_curenta = Accesare(ip_client=ip_client, full_url=full_url)
    parametrii_get = request.GET
    lista_nume_parametri = list(parametrii_get.keys())
    numar_parametri = len(lista_nume_parametri)
    tabel_headers = None
    tabel_rows = None

    tabel_param = request.GET.get('tabel')
    if tabel_param:
        toate_proprietatile = ['id', 'ip_client', 'pagina', 'url', 'data']
        
        if tabel_param.lower() == 'tot':
            tabel_headers = toate_proprietatile
        else:
            tabel_headers = [h.strip() for h in tabel_param.split(',')]

        tabel_rows = []
        for accesare in istoric_accesari:
            row_data = []
            for header in tabel_headers:
                if hasattr(accesare, header):
                    valoare = getattr(accesare, header)
                    if callable(valoare):
                        row_data.append(valoare())
                    else:
                        row_data.append(valoare)
                else:
                    row_data.append("N/A") 
            tabel_rows.append(row_data)
    cel_mai_putin_accesata = None
    cel_mai_mult_accesata = None

    if istoric_accesari:
        lista_pagini = [acc.pagina() for acc in istoric_accesari]
        
        frecvente = Counter(lista_pagini)
        
        cel_mai_putin_accesata = min(frecvente, key=frecvente.get)
        cel_mai_mult_accesata = max(frecvente, key=frecvente.get)
    context = {
        'data_html': data_html_string,
        'accesare_curenta': accesare_curenta,
        'numar_parametrii': numar_parametri,
        'lista_nume_parametri': lista_nume_parametri,
        'tabel_headers': tabel_headers,
        'tabel_rows': tabel_rows,
        'cel_mai_putin_accesata': cel_mai_putin_accesata,
        'cel_mai_mult_accesata': cel_mai_mult_accesata
    }
    return render(request,"aplicatie/info.html", context)

def afis_template(request):
    bloc_de_cod(request)
    
    return render(request,"templates/baza.html")

def afis_template2(request):
    bloc_de_cod(request)
    return render(request,"aplicatie/simplu.html")

def log_view(request):
    bloc_de_cod(request)
    numar_accesari = request.GET.get('ultimele')
    log_acces = list(reversed(istoric_accesari))
    error_message = None
    is_filtered_by_id = False 
    iduri_param_list = request.GET.getlist('iduri')
    log_entries=[]
    accesari_param = request.GET.get('accesari')
    numar_total_accesari=len(istoric_accesari)
    lista_detalii_accesari=None
    if accesari_param == 'detalii':
        lista_detalii_accesari = [acc.timestamp.strftime("%d %B %Y, ora %H")+" ID "+str(acc.id) for acc in istoric_accesari]
        # lista_noua=[]
        # for acc in istoric_accesari:
        #     lista_noua.append(acc.id)
        # lista_detalii_accesari = lista_noua

    if iduri_param_list:
        is_filtered_by_id = True
        toate_accesarile_dict = {str(acc.id): acc for acc in istoric_accesari}
        
        raw_id_list = []
        for id_group in iduri_param_list:
            raw_id_list.extend([id_str.strip() for id_str in id_group.split(',') if id_str.strip()])

        final_id_list = []
        if request.GET.get('dubluri') == 'true':
            final_id_list = raw_id_list
        else:
            seen_ids = set()
            for id_str in raw_id_list:
                if id_str not in seen_ids:
                    final_id_list.append(id_str)
                    seen_ids.add(id_str)
        
        for id_str in final_id_list:
            accesare_obj = toate_accesarile_dict.get(id_str)
            if accesare_obj:
                log_entries.append(accesare_obj)
    if numar_accesari is not None:
        n=int(numar_accesari)
        k=len(log_acces)
        if(n>k): # nu e bine
            error_message = f"Exista doar {k} accesari fata de {n} accesari cerute."
        else:
            log_acces=log_acces[:n]
    if is_filtered_by_id:
        log_acces=log_entries
    context = {
        'nr_accesari': numar_total_accesari,
        'log_entries': log_acces,
        'error_message': error_message,
        'filtrare': is_filtered_by_id,
        'lista_detalii_accesari': lista_detalii_accesari,
    }
    return render(request, 'aplicatie/log.html', context)

def afis_produse(request):
    ceasuri=Ceasuri.objects.all()
    form = FiltruCeasuriForm(request.GET)
    nr_elemente_pagina = 5
    mesaj_paginare = None
    if form.is_valid():
        data = form.cleaned_data
        if data['nr_pagini']:
            nr_elemente_pagina = int(data['nr_pagini'])
        
        paginare_anterioara = request.session.get('paginare_curenta', 5)

        if nr_elemente_pagina != paginare_anterioara:
            mesaj_paginare = "Atentie: In urma repaginarii este posibil sa fi sarit peste unele produse sau sa le vedeti din nou pe cele deja vizualizate."
        request.session['paginare_curenta'] = nr_elemente_pagina

        if data['nume_model']:
            ceasuri = ceasuri.filter(nume_model__icontains=data['nume_model'])
        if data['tip_geam']:
            ceasuri = ceasuri.filter(tip_geam__icontains=data['tip_geam'])
        if data['pret_min']:
            ceasuri = ceasuri.filter(pret__gte=data['pret_min'])
        if data['pret_max']:
            ceasuri = ceasuri.filter(pret__lte=data['pret_max'])
        if data['stoc_min']:
            ceasuri = ceasuri.filter(stoc__gte=data['stoc_min'])
        if data['stoc_max']:
            ceasuri = ceasuri.filter(stoc__lte=data['stoc_max']) 
        if data['diametru_min']:
            ceasuri = ceasuri.filter(diametru_carcasa__gte=data['diametru_min'])
        if data['diametru_max']:
            ceasuri = ceasuri.filter(diametru_carcasa__lte=data['diametru_max'])

        # Filtrare relatii (FK)
        if data['brand']:
            ceasuri = ceasuri.filter(brand=data['brand'])
        if data['mecanism']:
            ceasuri = ceasuri.filter(mecanism=data['mecanism'])
        if data['curea']:
            ceasuri = ceasuri.filter(curea=data['curea'])
        if data['oferta']:
            ceasuri = ceasuri.filter(oferta=data['oferta'])

        # Filtrare ManyToMany
        if data['caracteristici']:
            ceasuri = ceasuri.filter(caracteristici__in=data['caracteristici']).distinct()
    sortare='a'
    if(request.GET.get('sort')):
        sortare=request.GET.get('sort')
    if(sortare == 'a'):
        ceasuri=ceasuri.order_by('pret')
    else:
        ceasuri=ceasuri.order_by('-pret')

    paginator = Paginator(ceasuri, nr_elemente_pagina)
    page_number = request.GET.get('page')
    pagina_produse = paginator.get_page(page_number)
    context={
        "pagina_produse":pagina_produse,
        "form": form,
        "mesaj_paginare": mesaj_paginare,
    }
    return render(request, "aplicatie/ceasuri.html",context)

def afisare_detalii_produs(request, nume_model):
    ceasuri=Ceasuri.objects.filter(nume_model=nume_model)
    # ceasuri=get_object_or_404(Ceasuri,nume_mode=nume_model)
    if not ceasuri.exists():
        raise Http404("Niciun produs găsit cu acest nume de model.")
    nevoie='p'
    context = {
        'ceasuri': ceasuri,
        'nevoie': nevoie,
    }
    return render(request, "aplicatie/detalii.html",context)

def afis_categorii(request):
    categorii=Brand.objects.all()
    
    context={
        'categorii':categorii,
    }
    return render(request, "aplicatie/categorii.html",context)

def afis_categorii_spec(request, nume_brand):
    brand_curent = get_object_or_404(Brand, nume_brand=nume_brand)
    mesaj_eroare = None

    if 'brand' in request.GET:
        try:
            id_trimis = int(request.GET.get('brand'))
            if id_trimis != brand_curent.id:
                mesaj_eroare = f"Eroare de securitate: Ati incercat sa modificati manual categoria (ID trimis: {id_trimis}, ID asteptat: {brand_curent.id})."
        except ValueError:
            mesaj_eroare = "ID invalid."
    if request.GET:
        form = FiltruCeasuriForm(request.GET)
    else:
        form = FiltruCeasuriForm(initial={'brand': brand_curent})
    form.fields['brand'].widget = forms.HiddenInput()
    form.initial['brand'] = brand_curent

    ceasuri = Ceasuri.objects.filter(brand=brand_curent)

    if form.is_valid():
        data = form.cleaned_data
        
        if data.get('nume_model'):
            ceasuri = ceasuri.filter(nume_model__icontains=data['nume_model'])
        if data.get('tip_geam'):
            ceasuri = ceasuri.filter(tip_geam__icontains=data['tip_geam'])
        if data.get('pret_min'):
            ceasuri = ceasuri.filter(pret__gte=data['pret_min'])
        if data.get('pret_max'):
            ceasuri = ceasuri.filter(pret__lte=data['pret_max'])
            
        if data.get('stoc_min'):
            ceasuri = ceasuri.filter(stoc__gte=data['stoc_min'])
        if data.get('stoc_max'):
            ceasuri = ceasuri.filter(stoc__lte=data['stoc_max'])
            
        if data.get('diametru_min'):
            ceasuri = ceasuri.filter(diametru_carcasa__gte=data['diametru_min'])
        if data.get('diametru_max'):
            ceasuri = ceasuri.filter(diametru_carcasa__lte=data['diametru_max'])
            
        if data.get('mecanism'):
            ceasuri = ceasuri.filter(mecanism=data['mecanism'])
        if data.get('curea'):
            ceasuri = ceasuri.filter(curea=data['curea'])
        if data.get('oferta'):
            ceasuri = ceasuri.filter(oferta=data['oferta'])
            
        if data.get('caracteristici'):
            ceasuri = ceasuri.filter(caracteristici__in=data['caracteristici']).distinct()

    sortare = request.GET.get('sort', 'a')
    if sortare == 'a':
        ceasuri = ceasuri.order_by('pret')
    else:
        ceasuri = ceasuri.order_by('-pret')

    nr_elemente_pagina = 5
    mesaj_paginare = None

    if form.is_valid() and form.cleaned_data.get('nr_pagini'):
        nr_elemente_pagina = int(form.cleaned_data['nr_pagini'])
    session_key = f'paginare_brand_{brand_curent.id}'
    paginare_anterioara = request.session.get(session_key, 5)
    
    if nr_elemente_pagina != paginare_anterioara:
         mesaj_paginare = "Atentie: In urma repaginarii este posibil sa fi sarit peste unele produse."
    request.session[session_key] = nr_elemente_pagina

    paginator = Paginator(ceasuri, nr_elemente_pagina)
    page_number = request.GET.get('page')
    pagina_produse = paginator.get_page(page_number)

    context = {
        "pagina_produse": pagina_produse,
        "form": form,
        "mesaj_paginare": mesaj_paginare,
        "brand_curent": brand_curent, 
        "mesaj_eroare": mesaj_eroare,
    }
    
    return render(request, "aplicatie/ceasuri.html", context)

def afis_contact(request):
    mesaj_succes = None
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            date_salvare = form.cleaned_data.copy()
            
            if 'confirm_email' in date_salvare:
                del date_salvare['confirm_email']

            data_nasterii = date_salvare['data_nasterii']
            today = date.today()
            
            luni_totale = (today.year - data_nasterii.year) * 12 + (today.month - data_nasterii.month)
            
            if today.day < data_nasterii.day:
                luni_totale -= 1
            
            ani = luni_totale // 12
            luni = luni_totale % 12
            
            date_salvare['varsta'] = f"{ani} ani și {luni} luni"
            del date_salvare['data_nasterii']

            msg = date_salvare['mesaj']
            
            msg = msg.replace('\n', ' ').replace('\r', '')
            
            msg = re.sub(r'\s+', ' ', msg)
            
            date_salvare['mesaj'] = msg.strip()

            msg = date_salvare['mesaj']
            mesaj_nou = ""
            urmeaza_majuscula = True 

            for char in msg:
                if char.isalpha() and urmeaza_majuscula:
                    mesaj_nou += char.upper()
                    urmeaza_majuscula = False
                else:
                    mesaj_nou += char
                    if char in ".?!…":
                        urmeaza_majuscula = True
                    elif char.isalnum(): 
                        urmeaza_majuscula = False

            date_salvare['mesaj'] = mesaj_nou
                
            tip = date_salvare.get('tip_mesaj')
            zile = date_salvare.get('minim_zile_asteptare')
            este_urgent = False
            
            if tip in ['review', 'cerere'] and zile == 4:
                este_urgent = True
            elif tip == 'intrebare' and zile == 2:
                este_urgent = True
                
            date_salvare['urgent'] = este_urgent

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            date_salvare['ip_adresa'] = ip
            date_salvare['data_ora_sosire'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            nume_aplicatie = 'aplicatie'
            folder_mesaje = os.path.join(settings.BASE_DIR, nume_aplicatie, 'Mesaje')
            
            if not os.path.exists(folder_mesaje):
                os.makedirs(folder_mesaje)

            timestamp = int(time.time())
            sufix = "_urgent" if este_urgent else ""
            nume_fisier = f"mesaj_{timestamp}{sufix}.json"
            path_fisier = os.path.join(folder_mesaje, nume_fisier)

            try:
                with open(path_fisier, 'w', encoding='utf-8') as f:
                    json.dump(date_salvare, f, indent=4, ensure_ascii=False, default=str)
                
                mesaj_succes = f"Mesajul a fost salvat cu succes în fișierul: {nume_fisier}"
                form = ContactForm() # Resetam formularul
                
            except Exception as e:
                mesaj_succes = f"Eroare la salvarea fișierului: {e}"

    else:
        form = ContactForm()
    context={
        'form': form,
        'mesaj_succes': mesaj_succes
    }
    return render(request, 'aplicatie/contact.html', context)


def inregistrare(request):
    if request.method == 'POST':
        form = UtilizatorInregistrareForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            cod_generat = str(uuid.uuid4())
            user.cod = cod_generat
            user.email_confirmat = False
            user.save()

            domain = request.build_absolute_uri('/')[:-1] 
            link = f"{domain}/aplicatie/confirma_mail/{cod_generat}/"

            context_email = {
                'prenume': user.first_name,
                'nume': user.last_name,
                'username': user.username,
                'link_confirmare': link
            }
            
            html_message = render_to_string('aplicatie/confirmare_email.html', context_email)
            plain_message = strip_tags(html_message)
            subiect = "Confirmare cont - Site-ul Nostru"
            email_from = settings.EMAIL_HOST_USER
            destinatar = [user.email]

            send_mail(
                subiect,
                plain_message,
                email_from,
                destinatar,
                html_message=html_message, 
                fail_silently=False,
            )
            messages.success(request, f"Cont creat cu succes! Verifică adresa {user.email} pentru a activa contul.")
            return redirect('index')
        else:
            messages.error(request, "Va rugam sa corectati erorile de mai jos.")
    else:
        form = UtilizatorInregistrareForm()
    context={
        'form': form
    }
    return render(request, 'aplicatie/inregistrare.html', context)

def view_confirma_mail(request, cod):
    rezultat = valideaza_si_activeaza_cod(cod)
    
    if rezultat is True:
        return render(request, 'aplicatie/confirmare_succes.html')
    else:
        return render(request, 'aplicatie/confirmare_esec.html', {'mesaj': 'Cod invalid sau expirat.'})


def login_view(request):
    if request.method == 'POST':
        form = LoginFormPersonalizat(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.email_confirmat:  
                
                login(request, user) 

                if form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(86400)
                else:
                    request.session.set_expiry(0)

                date_sesiune = {
                    'username': user.username,
                    'email': user.email,
                    'nume_complet': f"{user.first_name} {user.last_name}",
                    'data_inscriere': str(user.date_joined.strftime("%d-%m-%Y")),
                    'telefon': getattr(user, 'telefon', 'Nespecificat'),
                    'adresa': getattr(user, 'adresa', 'Nespecificat'),
                }
                request.session['date_utilizator'] = date_sesiune

                messages.success(request, f"Bine ai venit, {user.username}!")
                return redirect('profil')
            
            else:
                messages.error(request, "Te rugăm să confirmi adresa de e-mail înainte de a te loga.")
                return redirect('login') 
    else:
        form = LoginFormPersonalizat()
    
    return render(request, 'aplicatie/login.html', {'form': form})

def logout_view(request):
    try:
        del request.session['date_utilizator']
    except KeyError:
        pass
        
    logout(request)
    messages.info(request, "Te-ai delogat cu succes.")
    return redirect('index')

@login_required
def profil_view(request):
    date_utilizator = request.session.get('date_utilizator', {})
    
    if not date_utilizator:
        user = request.user
        date_utilizator = {
            'username': user.username,
            'email': user.email,
            'telefon': getattr(user, 'telefon', '-'),
        }

    return render(request, 'aplicatie/profil.html', {'date_utilizator': date_utilizator})

@login_required
def schimbare_parola_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Parola a fost schimbată cu succes!')
            return redirect('profil')
        else:
            messages.error(request, 'Te rugăm să corectezi erorile.')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'aplicatie/schimbare_parola.html', {'form': form})