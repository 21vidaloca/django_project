from django.shortcuts import render
import locale
from datetime import datetime
from collections import Counter
from .clase import Accesare
from django.http import HttpResponse
def index(request):
	return HttpResponse("Primul raspuns")
try:
    locale.setlocale(locale.LC_TIME, 'ro_RO.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')
istoric_accesari=[]
def bloc_de_cod(request):
    ip_client = request.META.get('REMOTE_ADDR')
    full_url = request.get_full_path()
    istoric_accesari.append(Accesare(ip_client=ip_client, full_url=full_url))
def afis_data(valoare_parametru):
    
    acum = datetime.now()
    data_formatata = acum.strftime("%A, %d %B %Y").capitalize()
    ora_formatata = acum.strftime("%H:%M:%S")

    html_output = '<h2>Data și ora</h2>'
    
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

    # --- Logica NOUĂ pentru parametrul 'tabel' ---
    tabel_param = request.GET.get('tabel')
    if tabel_param:
        toate_proprietatile = ['id', 'ip_client', 'pagina', 'url', 'data']
        
        # Determinăm ce coloane (antete) să afișăm
        if tabel_param.lower() == 'tot':
            tabel_headers = toate_proprietatile
        else:
            tabel_headers = [h.strip() for h in tabel_param.split(',')]

        # Pregătim rândurile tabelului
        tabel_rows = []
        for accesare in istoric_accesari:
            row_data = []
            for header in tabel_headers:
                # Folosim getattr pentru a accesa dinamic proprietatea sau metoda obiectului
                if hasattr(accesare, header):
                    valoare = getattr(accesare, header)
                    # Dacă e o metodă (ca url() sau pagina()), o apelăm
                    if callable(valoare):
                        row_data.append(valoare())
                    else:
                        row_data.append(valoare)
                else:
                    row_data.append("N/A") # Adăugăm N/A dacă proprietatea nu există
            tabel_rows.append(row_data)
    cel_mai_putin_accesata = None
    cel_mai_mult_accesata = None

    # Calculăm frecvențele doar dacă există accesări înregistrate
    if istoric_accesari:
        # Extragem calea fiecărei pagini accesate
        lista_pagini = [acc.pagina() for acc in istoric_accesari]
        
        # Numărăm de câte ori apare fiecare pagină
        frecvente = Counter(lista_pagini)
        
        # Găsim pagina cu cele mai puține și cele mai multe accesări
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
    return render(request,"templates/baza.html",
        {
            "titlu_tab":"Titlu fereastra",
            "titlu_articol":"Titlu afisat",
            "continut_articol":"Continut text"
        }
    )


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
        lista_detalii_accesari = [acc.timestamp.strftime("%d %B %Y, ora %H:%M:%S") for acc in istoric_accesari]

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
        
    }
    return render(request, 'aplicatie/log.html', context)
