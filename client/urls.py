from django.urls import path
from . import views
urlpatterns = [
     #path('Inscription_Client', views.InscriptionClient, name='Inscription_Client'),
      path('Inscrip_client', views.Inscrip_client, name='Inscrip_client'),
      path('loginclient', views.loginclient, name='loginclient'),
      path('lougout', views.lougout, name="lougout"),
      path('login_prestation', views.login_prestation, name="login_prestation"),

      #path('vue_profil', views.vue_profil, name='vue_profil'),
]
