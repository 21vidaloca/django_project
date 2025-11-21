from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"),
    path("info", views.info, name="info"),
    path("baza", views.afis_template, name="baza"),
    path("simplu", views.afis_template2, name="simplu"),
    path("log", views.log_view, name="log_page"),
    path("produse",views.afis_produse, name="produse"),
    path('produse/<str:nume_model>/', views.afisare_detalii_produs, name='detaliu-produs'),
    path("categorii", views.afis_categorii,name="categorii"),
    path("categorii/<str:nume_brand>", views.afis_categorii_spec,name="detalii_categorii"),
    path('despre/', views.pagina_despre, name='despre'),
    path('contact/', views.pagina_in_lucru, name='contact'),
    path('termeni/', views.pagina_in_lucru, name='termeni'),
    path('cos-cumparaturi/', views.pagina_in_lucru, name='cos'),
]
