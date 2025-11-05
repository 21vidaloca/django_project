from django.contrib import admin
from .models import Caracteristici
from .models import Brand
from .models import Oferta
from .models import Curea
from .models import Mecanism
from .models import Ceasuri
# Register your models here.

class CeasuriAdmin(admin.ModelAdmin):
    list_display = ('pret', 'nume_model', 'stoc', 'tip_geam') 
    list_filter = ('stoc','pret')
    search_fields = ('nume_model', 'tip_geam')
    fieldsets= (
        ('Date generale', {
            'fields': ('nume_model','pret')
        }),
        ('Date specifice', {
            'fields': ('stoc','tip_geam'),
            'classes': ('collapse',)
        })
    )
    ordering = ('-pret',)
    list_per_page = 5
admin.site.register(Ceasuri, CeasuriAdmin)
admin.site.register(Caracteristici)
admin.site.register(Brand)
admin.site.register(Oferta)
admin.site.register(Curea)
admin.site.register(Mecanism)

# admin.site.register(Ceasuri)