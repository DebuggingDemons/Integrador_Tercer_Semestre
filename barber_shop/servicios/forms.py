from django import forms

def servicios(request):
    form = formularioDeLogin
    return render(request, 'servicios/servicios.html', {'form':form})

    
