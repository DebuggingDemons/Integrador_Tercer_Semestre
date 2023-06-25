from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Turnos.urls')),
    path('usuarios/', include('Usuarios.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
