from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Caracteristici
from .models import Brand
from .models import Oferta
from .models import Curea
from .models import Mecanism
from .models import Ceasuri
# Register your models here.
class UtilizatorAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informații Suplimentare', {
            'fields': ('telefon', 'adresa', 'oras', 'cod_postal', 'data_nasterii', 'abonat_newsletter'),
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informații Suplimentare', {
            'fields': ('email', 'telefon', 'adresa'),
        }),
    )


class CeasuriAdmin(admin.ModelAdmin):
    list_display = ('pret', 'nume_model', 'stoc', 'tip_geam') 
    list_filter = ('stoc','pret')
    search_fields = ('nume_model', 'tip_geam')
    fieldsets= (
        ('Date generale', {
            'fields': ('nume_model','pret','brand', 'poza')
        }),
        ('Date specifice', {
            'fields': ('stoc','tip_geam', 'diametru_carcasa'),
            'classes': ('collapse',)
        })
    )
    ordering = ('-pret',)
    list_per_page = 5
admin.site.register(CustomUser, UtilizatorAdmin)
admin.site.register(Ceasuri, CeasuriAdmin)
admin.site.register(Caracteristici)
admin.site.register(Brand)
admin.site.register(Oferta)
admin.site.register(Curea)
admin.site.register(Mecanism)

# admin.site.register(Ceasuri)