from django.urls import path

from Usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # (temlate, vista, nombre dentro de un html)
    
    path('login/', view=views.login, name='login'),
    path('registro/', view=views.registro, name='registro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', view=views.home, name='logout'),
]