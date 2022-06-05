from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class prestataire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    gender_choice = (
        ("male", "Homme"),
        ("Female", "Femme"),
    )
    gender = models.CharField(choices=gender_choice, default="male", max_length=10)
    date_naissance = models.DateField(null=True)
    special = (
        ("Electrique", "Electrique"),
        ("Mécanique_Auto", "Mecanique"),
        ("Climatisation", "Climatisation"),
        ("Plombérie", "Plombérie"),
        ("Menuiserie", "Menuiserie"))
    Specialite = models.CharField(choices=special, default="------", max_length=20, null=True)
    annee_experience = models.PositiveIntegerField(null=True)
    cv = models.FileField(upload_to='CV/', null=True)
    NNI = models.CharField(max_length=10, null=True)
    Date_inscription = models.DateTimeField(null=True, auto_now_add=True)
    num_tel=models.CharField(max_length=40, null=True)
    statut = models.CharField(max_length=40, default="P")
    def __str__(self):
        return self.nom
