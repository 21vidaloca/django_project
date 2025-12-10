from django.contrib.auth import get_user_model
def valideaza_si_activeaza_cod(cod):
    User = get_user_model()
    
    try:
        user = User.objects.get(cod=cod)
        if not user.email_confirmat:
            user.email_confirmat = True
            user.cod = '' 
            user.save()
            
        return True
        
    except User.DoesNotExist:
        return False