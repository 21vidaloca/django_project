from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"),
    path("info", views.info, name="info"),
    path("baza", views.afis_template, name="baza"),
    path("simplu", views.afis_template2, name="simplu"),
    path("log", views.log_view, name="log_page"),
    path("produse",views.afis_produse, name="produse"),
    path('produse/<int:produs_id>/', views.afisare_detalii_produs, name='detaliu-produs'),
]
