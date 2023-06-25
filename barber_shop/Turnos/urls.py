from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Turnos import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # (temlate, vista, nombre dentro de un html)
    
    path('', view=views.home, name='home'),
    path('turnos/', view=views.turnos, name='turnos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    