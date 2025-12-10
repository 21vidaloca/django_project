from django.contrib import admin
from django.urls import path, include
from django.conf import settings              # <--- IMPORT IMPORTANT 1
from django.conf.urls.static import static
admin.site.site_header = "Administrare Magazin de Ceasuri"
admin.site.site_title = "Panou Admin"
admin.site.index_title = "Bun venit in panoul de control"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicatie/', include("aplicatie.urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)