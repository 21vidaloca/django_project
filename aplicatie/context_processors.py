from .models import Brand  

def meniu_categorii(request):
    toate_categoriile = Brand.objects.all().order_by('nume_brand')
    return {
        'toate_categoriile_meniu': toate_categoriile
    }