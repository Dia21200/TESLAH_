from django.forms import ModelForm
from .models import prestation,publication,Specialite,commentaire,image_publication
from django import forms

special=[
        ("Default", ""),
        ("Electrique", "Electrique"),
        ("Mécanique_Auto", "Mécanique_Auto"),
        ("Climatisation", "Climatisation"),
        ("Plombérie", "Plombérie"),
        ("Menuiserie", "Menuiserie")
]

class prestationForm(ModelForm):

    num_telephone = forms.IntegerField(label="Numéro de téléphone:", help_text='', required=True,
                               widget=forms.TextInput(
                                   attrs={"class": "form-control","name":"u_name", "id": "u_name",
                                          "placeholder": "Votre numéro de téléphone",
                                          }))

    Adress = forms.CharField(label="Ville & Adress:", max_length=40, help_text='', required=True,
                              widget=forms.TextInput(
                                  attrs={"class": "form-control", "id": "Adresse",
                                         "placeholder": "par exemple: Nouakchott,Ksar",
                                         }))

    Service = forms.ChoiceField(label="Spécialité:",
                                   help_text='',
                                   required=True,
                                   choices=special, widget=forms.Select(
            attrs={"class": "form-control", "id": "Adresse", "placeholder": "slect",
                   }))

    Description = forms.CharField(label="Ville & Adress:", help_text='', required=True,
                              widget=forms.Textarea(
                                  attrs={"class": "form-control", "id": "Adresse",
                                         "placeholder": "Faites une description de vos problémes",'rows':5
                                         }))

    class Meta:
        model = prestation
        fields = ['num_telephone', 'Adress', 'Service','Description']

#-------------------------------------------------# ------------------------------------------------------------------------------
class publicationForm(ModelForm):
    Description = forms.CharField(label="", help_text='', required=True,
                                  widget=forms.Textarea(
                                      attrs={"class": "form-control", "id": "Adresse",
                                             "placeholder": "Faites une description.....", 'rows': 2
                                             }))

    Lieu = forms.CharField(label="", help_text='', required=True,
                                  widget=forms.Textarea(
                                      attrs={"class": "form-control", "id": "Adresse",
                                             "placeholder": "Lieu", 'rows': 1
                                             }))

    photos = forms.ImageField(label="", required=True,
                              widget=forms.FileInput(
                                  attrs={"class": "custom-file-input","id":"customFile","placeholder": "",'multiple':True,
                                         }))

    class Meta:
        model=publication
        fields = ['Description', 'Lieu','photos' ]


class specialitform(ModelForm):

    specialite = forms.ChoiceField(
                                help_text='',
                                required=True,
                                choices=special, widget=forms.Select(
            attrs={"class": "form-control rounded-corner", "id": "Adresse",}))
    class Meta:
        model=Specialite
        fields = ['specialite']

class commentaireform(ModelForm):

    Comment = forms.CharField(label="", help_text='', required=True,
                                  widget=forms.Textarea(
                                      attrs={"class": "form-control rounded-corner",
                                             "placeholder": "faites vos commentaires",
                                             }))
    class Meta:
        model=Specialite
        fields = ['Comment']

class imageForm(ModelForm):
    photos = forms.ImageField(label="", required=True,
                              widget=forms.FileInput(
                                  attrs={"class": "custom-file-input","id":"customFile","placeholder": "",'multiple':True,
                                         }))
    class Meta:
        model=image_publication
        fields = ['photos']


class loginForm(forms.Form):
    username = forms.CharField(label="Numéro de téléphone :", max_length=8, help_text='', required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", "id": "exampleInputNumero", "placeholder": "Numéro de téléphone:",
                                                          }))
    password = forms.CharField(label="Mot de passe:", max_length=10, help_text='', required=True,
                              widget=forms.PasswordInput(
                                  attrs={"class": "form-control", "id": "password1", "placeholder": "mot de passe",
                                         }))