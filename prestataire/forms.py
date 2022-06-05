from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import prestataire

from django.utils.safestring import mark_safe



gender_choice = [
    ("Default", "--"),
    ("male", "Homme"),
    ("Female", "  Femme"),
]
special=[
        ("Default", "--"),
        ("Electrique", "Electrique"),
        ("Mécanique_Auto", "Mécanique_Auto"),
        ("Climatisation", "Climatisation"),
        ("Plombérie", "Plombérie"),
        ("Menuiserie", "Menuiserie")
]

class RegisterprestataireForm(forms.ModelForm):
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


class prestataireForm(forms.ModelForm):

    nom=forms.CharField(label="Nom complet:", max_length=40, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "Prenom", "placeholder": "Nom complet",
                                                         }))

    adresse = forms.CharField(label="Ville & Adress:", max_length=40, help_text='', required=True,
                              widget=forms.TextInput(
                                  attrs={"class": "form-control", "id": "Adresse",
                                         "placeholder": "par exemple: Nouakchott,Ksar"
                                         }))
    gender=forms.ChoiceField(label="Spécialité:",
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

    Specialite = forms.ChoiceField(label="Spécialité:",
                                   help_text='',
                                   required=True,
                                   choices=special, widget=forms.Select(
            attrs={"class": "form-control", "id": "Adresse", "placeholder": "select",
                   }))

    annee_experience = forms.CharField(label="Année d'expérience:", help_text='', required=True, max_length=2,
                                       widget=forms.TextInput(
                                           attrs={"class": "form-control", "id": "Adresse", "placeholder": "par exemple: 2ans",
                                                  }))

    NNI = forms.CharField(label="Numéro national:", help_text='', required=True, max_length=10,
                          widget=forms.TextInput(
                              attrs={"class": "form-control", "id": "Adresse", "placeholder": "Numéro national",
                                     }))

    cv = forms.FileField(label="Criculum Vitea (CV):", required=True,
                         widget=forms.FileInput(
                             attrs={"class": "col form-group","placeholder": "Inserez votre Cv",
                                    }))

    class Meta:
        model = prestataire
        fields=['nom','adresse','date_naissance','gender','Specialite','cv',
                'annee_experience','NNI']




class prestataire_loginForm(forms.Form):
    username = forms.CharField(label="Numéro de téléphone :", max_length=8, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "Prenom", "placeholder": "Numéro de téléphone:",
                                                          }))
    password = forms.CharField(label="Mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "mot de passe", "placeholder": "mot de passe",
                                         }))

