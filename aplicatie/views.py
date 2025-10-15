from django.shortcuts import render
import locale
from datetime import datetime
from .clase import Accesare
from django.http import HttpResponse
def index(request):
	return HttpResponse("Primul raspuns")
try:
    locale.setlocale(locale.LC_TIME, 'ro_RO.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')

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
    if 'data' in request.GET:
        valoare_parametru = request.GET.get('data', '')
        data_html_string = afis_data(valoare_parametru)
    ip_client = request.META.get('REMOTE_ADDR')
    full_url = request.get_full_path()
    
    accesare_curenta = Accesare(ip_client=ip_client, full_url=full_url)
    context = {
        'data_html': data_html_string,
        'accesare_curenta': accesare_curenta
    }
    return render(request,"aplicatie/info.html", context)

def afis_template(request):
    return render(request,"templates/baza.html",
        {
            "titlu_tab":"Titlu fereastra",
            "titlu_articol":"Titlu afisat",
            "continut_articol":"Continut text"
        }
    )


def afis_template2(request):
    return render(request,"aplicatie/simplu.html")
