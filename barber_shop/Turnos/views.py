from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html',{'saludo': 'Hola a todos'})

@login_required(login_url='login')
def turnos(request):
    
    user = request.user
    turnos = Turno.objects.filter(cliente = user)
    if request.user.is_authenticated:
        return render(request, 'turnos.html',{'turnos': turnos, 'vacio': 'No tiene turnos'})
    
    
    