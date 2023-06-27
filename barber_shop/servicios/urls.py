from django.urls import path
from servicios import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # (temlate, vista, nombre dentro de un html)
    path('servicios/', view=views.agregarServicio, name='servicios'),  
]
