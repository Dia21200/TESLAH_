from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    nom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40)
    gender_choice = (
        ("male", "Homme"),
        ("Female", "Femme"),)

    gender = models.CharField(choices=gender_choice, default="-----", max_length=10)
    date_naissance = models.DateField(null=True)
    Date_inscription = models.DateTimeField(null=True, auto_now_add=True)
    statut=models.CharField(max_length=40,default="C")
    def __str__(self):
        return self.nom


"""@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    instance.client.save()
"""

"""""
from django.contrib.auth.models import User
from django.db import models



class posti(models.Model):
    num_telephone = models.IntegerField(null=False, unique=True)
    Adress=models.CharField(max_length=255)
    Service=models.CharField(max_length=100)
    type=models.CharField(max_length=255)
    Description=models.TextField()
    Date=models.DateTimeField(null=True,default=win32timezone.now())
    id_client = models.ForeignKey(User, on_delete=models.CASCADE,unique=True,null=True)
"""""


















"""from django.db import models
from django.contrib import admin


class lient(models.Model):
    Prenom = models.CharField(max_length=25)
    Nom = models.CharField(max_length=25)
    Phone = models.CharField(max_length=8,unique=True)
    adresse = models.CharField(max_length=40)
    gender_choice = (
        ("male", "Homme"),
        ("Female", "Femme"),
    )
    gender = models.CharField(choices=gender_choice, default="-----", max_length=10)
    date_naissance = models.DateField(null=True)
    Password1 = models.CharField(max_length=10)
    Password2 = models.CharField(max_length=10)

                                          #Importation des données au nniveau du compte administrateur admin
class lientAdmin(admin.ModelAdmin):
    list_display = ('Prenom','Nom','Phone','adresse','gender','date_naissance','Password1','Password2')
    list_filter = ('Prenom','Nom','Phone','adresse')
    search_fields = ['adresse', 'num_telephone']
"""""