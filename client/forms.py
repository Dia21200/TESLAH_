from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import client

gender_choice = [
    ("Default", "--"),
    ("male", "Homme"),
    ("Female", "Femme"),
]

class RegisterclientForm(forms.ModelForm):
    username = forms.CharField(label="Numéro de Téléphone :", max_length=8, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "Telephone", "placeholder": "Numéro de Téléphone",
                                                          }))

    password = forms.CharField(label="Mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "mot de passe", "placeholder": "mot de passe",
                                         }))

    confirm_password = forms.CharField(label="Confirmation du mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "mot de passe", "placeholder": "Confirmer votre mot de passe",
                                         }))


    class Meta:
        model = User
        fields=['username','last_name','password']

    def save(self, commit=True):
        user = super().save(commit=True)
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password']

        if commit:
            user.save()
        return user


class clientForm(forms.ModelForm):

    nom = forms.CharField(label="Nom complet:", max_length=40, help_text='', required=True,
                          widget=forms.TextInput(
                              attrs={"class": "form-control", "id": "Prenom", "placeholder": "Nom complet",
                                     }))

    adresse = forms.CharField(label="Ville & Adress:", max_length=40, help_text='', required=True,
                              widget=forms.TextInput(
                                  attrs={"class": "form-control", "id": "Adresse",
                                         "placeholder": "par exemple: Nouakchott,Ksar",
                                         }))

    gender = forms.ChoiceField(label="Spécialité:",
                               help_text='',
                               required=True,
                               choices=gender_choice, widget=forms.Select(
            attrs={"class": "form-control", "id": "Adresse", "placeholder": "select",
                   }))

    date_naissance = forms.DateField(label="Date de naissance",
                                     help_text='',
                                     required=True,
                                     widget=forms.DateInput(
                                         attrs={"class": "form-control", "type": "date", "id": "date_de_naissance",
                                                "placeholder": "Votre date de naissance",
                                                "data-sb-validations": "required"}))

    class Meta:
        model = client
        fields=['nom','adresse','date_naissance','gender']

class client_loginForm(forms.Form):
    username = forms.CharField(label="Numéro de téléphone :", max_length=8, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "Prenom", "placeholder": "Numéro de téléphone:",
                                                          }))
    password = forms.CharField(label="Mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "mot de passe", "placeholder": "mot de passe",
                                         }))






"""from django.forms import ModelForm
from .models import lient
from django import forms

gender_choice = [
    ("Default", "--"),
    ("male", "Homme"),
    ("Female", "Femme"),
]

special=[
        ("Default", "--"),
        ("Electrique", "Electrique"),
        ("Mécanique_Auto", "Mecanique"),
        ("Climatisation", "Climatisation"),
        ("Plombérie", "Plombérie"),
        ("Menuiserie", "Menuiserie")
]

#-----------------------------------------------------------------------------------------------------------------------
                                                #Formulaire client
class ClientForm(ModelForm):
    Prenom = forms.CharField(label="Prénom :", max_length=25, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "Prenom", "placeholder": "Prénom:",
                                                         }))
    Nom = forms.CharField(label="Nom :", max_length=25, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "nom", "placeholder": "Nom",
                                                         }))
    Phone = forms.IntegerField(label="Numéro de téléphone :", help_text='', required=True,
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", "id": "nom", "placeholder": "Votre numéro de téléphone",
                                          }))
    gender = forms.ChoiceField(label="Genre",
                               help_text='',
                               required=True,
                               choices=gender_choice,widget=forms.Select(
                                  attrs={"class": "form-control", "id": "Adresse", "placeholder": "par exemple: Nouakchott,Ksar",
                                         }))

    date_naissance = forms.DateField(label="Date de naissance",
                                     help_text='',
                                     required=True,
                                     widget=forms.DateInput(
                                         attrs={"class": "form-control", "type": "date", "id": "date_de_naissance",
                                                "placeholder": "Votre date de naissance",
                                                "data-sb-validations": "required"}))

    adresse = forms.CharField(label="Ville & Adress:", max_length=40, help_text='', required=True,
                              widget=forms.TextInput(
                                  attrs={"class": "form-control", "id": "Adresse", "placeholder": "par exemple: Nouakchott,Ksar",
                                         }))

    Password1 = forms.CharField(label="Mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "mot de passe", "placeholder": "mot de passe",
                                         }))

    Password2 = forms.CharField(label="Confirmation du mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "mot de passe", "placeholder": "Confirmer votre mot de passe",
                                         }))

    class Meta:
        model = lient
        fields=['Prenom','Nom','Phone','adresse','gender','date_naissance','Password1','Password2']
"""""