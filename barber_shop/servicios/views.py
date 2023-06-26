from django.shortcuts import render

# Create your views here.

def servicios(request):
    form = formularioDeLogin
    return render(request, 'servicios/servicios.html', {'form':form})

    
