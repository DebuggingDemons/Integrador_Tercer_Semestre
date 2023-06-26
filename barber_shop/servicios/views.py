from django.shortcuts import render

# Create your views here.

def servicios(request):
    form = formularioDeServicio
    return render(request, 'servicios/servicios.html', {'form':form})

    
