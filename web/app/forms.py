from . models import Connexion
from django import forms

class ConnexionForm(forms.ModelForm):
    class Meta:
        model = Connexion

        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class':'forms-control', 'placeholder': 'votre email ou numéro de téléphone'}),
            'password': forms.PasswordInput(attrs={'class':'forms-control', 'placeholder': 'votre mot de passe'})
        }