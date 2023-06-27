from django.urls import path
from servicios import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # (temlate, vista, nombre dentro de un html)
    path('servicios/', view=views.agregarServicio, name='servicios'),
    path('servicios/mostrar_servicio', view=views.mostrarServicio, name='mostrar_servicio'),
]
