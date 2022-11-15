from django.shortcuts import render
from . forms import ConnexionForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        form = ConnexionForm(request.POST)
        if form.is_valid:
            form.save()
        else:
            messages.error("votre saisi est incorrect")

    form = ConnexionForm()
    context = {'form': form}
    return render(request, 'app/index.html', context)
