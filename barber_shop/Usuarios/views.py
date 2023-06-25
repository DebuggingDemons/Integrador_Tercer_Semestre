from django.shortcuts import render
from .forms import formularioDeLogin, formularioDeREgistro
from .models import AbstractUser, Usuario

# Create your views here.
def login(request):
    form = formularioDeLogin
    return render(request, 'registration/login.html', {'form':form})


def registro(request):
    if request.POST:
        
        user =  request.POST['usuario']
        password =  request.POST['password']
        nombre =  request.POST['nombre']
        apellido =  request.POST['apellido']
        email =  request.POST['email']
        esBarbero =  request.POST['esBarbero']
        
        usuario  = Usuario.objects.create_user(user, email, password)
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.esBarbero = esBarbero
        
        super = request.POST['super']
        if super:
            usuario.is_staff = True
        
        usuario.save()
        form = formularioDeLogin
        return render(request,'registration/login.html',{'form':form})
    
    
    form =  formularioDeREgistro
    return render(request,'registration/registro.html', {'form':form})
