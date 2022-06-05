from django.utils import timezone
from django.db import models
from prestataire.models import prestataire
from client.models import client
from .models import *
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
import decimal
from django.contrib.auth.models import User
from django.contrib import admin
from django.conf import settings



#----------------------------------------------------------------------------------------------------------------------------

class prestation(models.Model):
    num_telephone = models.IntegerField(null=False, unique=True)
    Adress=models.CharField(max_length=255)
    Service=models.CharField(max_length=100)
    type=models.CharField(max_length=255)
    Description=models.TextField()
    Date=models.DateTimeField(null=True,auto_now_add=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

class consulter(models.Model):
    #id_client=models.ForeignKey(Client, on_delete=models.CASCADE)
    id_prestataire=models.ForeignKey(prestataire, on_delete=models.CASCADE)

#--------------------------------------------------------------------------------------------------------------------------

class service(models.Model):
   electricite=models.CharField(max_length=100)

class prix(models.Model):
   prix=models.IntegerField()
#-----------------------------------------------------------------------------------------------------------------------------
class publication(models.Model):
    Description = models.TextField()
    photos = models.ImageField(upload_to='image/', null=True,blank=True)
    Date_pub = models.DateTimeField(auto_now_add=True)
    Lieu = models.CharField(max_length=200)
    prestataire = models.ForeignKey(User, on_delete=models.CASCADE)

#----------------------------------------------------------------------------------------------------------------------------------------
                                                          #Modele Image
class image_publication(models.Model):
   publication=models.ForeignKey(publication, on_delete=models.CASCADE,default=None)
   photos = models.ImageField(upload_to='image/')


   def __str__(self):
       return self.publication.Description
#----------------------------------------------------------------------------------------------------------------------------------------
                                                          #Modele commentaire
class commentaire(models.Model):
   Comment=models.TextField()
   date_comments=models.DateTimeField(auto_now_add=True)
   publi= models.ForeignKey(publication, on_delete=models.CASCADE)
   client=models.ForeignKey(client, on_delete=models.CASCADE)

class Specialite(models.Model):
    specialite=models.CharField(max_length=100)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
