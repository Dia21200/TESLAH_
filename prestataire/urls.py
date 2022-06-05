from django.urls import path
from . import views
urlpatterns = [
      path('Inscrip_prestataire', views.Inscrip_prestataire, name='Inscrip_prestataire'),
      path('loginprestataire', views.loginprestataire, name='loginprestataire'),
      path('lougout', views.lougout, name="lougout"),

]
