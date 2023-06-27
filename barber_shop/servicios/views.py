from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicios

# Create your views here.

def agregarServicio(request):
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']

        servicio = Servicios(nombre=nombre, precio=precio, descripcion=descripcion)
        servicio.save()
    return render(request, 'servicios.html')


def mostrarServicio(request):
    servicios = Servicios.objects.all()
    return render(request, 'mostrar_servicio.html', {'servicios': servicios})




def eliminarServicio(request, id):
    servicios = get_object_or_404(Servicios, idServicio=id)

    if request.method == 'POST':
        servicios.delete()
        return redirect('mostrar_servicio')
    return render(request, 'mostrar_servicio.html', {'servicios': servicios})