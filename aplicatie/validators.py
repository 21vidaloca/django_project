import re
from datetime import date, datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# a. Validator Varsta (Major)
def validate_varsta_majora(data_nasterii):
    if not data_nasterii:
        return
    today = date.today()
    varsta = today.year - data_nasterii.year - ((today.month, today.day) < (data_nasterii.month, data_nasterii.day))
    if varsta < 18:
        raise ValidationError(f"Trebuie sa aveti peste 18 ani. Varsta calculata este {varsta} ani.")

# b. & c. Validator Mesaj (Nr cuvinte și Lungime cuvinte)
def validate_mesaj_text(text):
    if not text:
        return
    cuvinte = re.findall(r'\w+', text)
    numar_cuvinte = len(cuvinte)

    # b. Intre 5 și 100 cuvinte
    if not (5 <= numar_cuvinte <= 100):
        raise ValidationError(f"Mesajul trebuie sa contină intre 5 si 100 de cuvinte. Ati scris {numar_cuvinte} cuvinte.")
    
    # c. Lungimea unui cuvant max 15
    for cuvant in cuvinte:
        if len(cuvant) > 15:
            raise ValidationError(f"Cuvantul '{cuvant}' este prea lung. Maxim 15 caractere permise per cuvant.")

# d. Validator Fara Link-uri
def validate_fara_linkuri(text):
    if not text:
        return
    for cuvant in text.split():
        if cuvant.lower().startswith(('http://', 'https://')):
            raise ValidationError("Nu sunt permise link-uri (http/https) in text.")

# e. Validator Tip Mesaj
def validate_tip_mesaj_selectat(valoare):
    if valoare == 'neselectat':
        raise ValidationError("Va rugam sa selectați un tip de mesaj valid.")

# f. & g. Validator CNP (Cifre + Structura 1/2 + Data)
def validate_cnp_custom(cnp):
    if not cnp:
        return 
    
    # f. Doar cifre
    if not cnp.isdigit():
        raise ValidationError("CNP-ul trebuie sa contina doar cifre.")
    
    # g. Structură (Începe cu 1 sau 2, și data validă)
    if not cnp.startswith(('1', '2')):
        raise ValidationError("CNP-ul trebuie sa inceapa cu cifra 5 sau 6.")
    
    data_str = cnp[1:7] # AALLZZ
    try:
        an = "19" + data_str[0:2]
        luna = data_str[2:4]
        ziua = data_str[4:6]
        datetime(year=int(an), month=int(luna), day=int(ziua))
    except ValueError:
        raise ValidationError("CNP-ul contine o data invalida (cifrele 2-7).")

# h. Validator Email Temporar
def validate_email_netemporar(email):
    if not email:
        return
    domenii_interzise = ['guerillamail.com', 'yopmail.com']
    try:
        domeniu = email.split('@')[1]
        if domeniu in domenii_interzise:
            raise ValidationError(f"Domeniul {domeniu} nu este permis (email temporar).")
    except IndexError:
        pass

# i. Validator Format Text
def validate_inceput_majuscula_si_caractere(text):
    if not text:
        return
    if not re.match(r'^[A-Z][a-zA-Z\s\-]*$', text):
        raise ValidationError("Textul trebuie sa inceapă cu litera mare si sa contină doar litere, spatii sau cratime.")

# j. Validator Capitalizare după spatiu/cratima
def validate_capitalizare_parti(text):
    if not text:
        return
    parti = re.split(r'[\s\-]', text)
    
    for parte in parti:
        if parte and not parte[0].isupper():
            raise ValidationError(f"Fiecare nume/prenume trebuie sa inceapa cu litera mare (Eroare la: '{parte}').")
        
def validate_fara_simboluri(value):
    simboluri_interzise = ['@', '#', '$']
    for simbol in simboluri_interzise:
        if simbol in str(value):
            raise ValidationError(f"Simbolul '{simbol}' nu este permis in acest camp.")

def validate_fara_cuvantul_ceas(value):
    if 'ceas' in str(value).lower():
        raise ValidationError("Nu includeti cuvântul 'ceas' in nume. Este redundant.")