
from django.contrib import messages
from django.shortcuts import render, redirect
#from django.core.urlresolvers import reverse
from . models import *
from prestataire.models import prestataire
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from .formulaire import prestationForm,publicationForm,specialitform,commentaireform,loginForm,imageForm
from prestataire.views import loginprestataire
from client.views import loginclient
from rest_framework.decorators import api_view
from django.urls import reverse_lazy
from django.http import HttpResponse #Redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import modelform_factory


#-----------------------------------------------------------------------------------------------------------------------
                                                                #Prestation
def prestation(request):
    if not request.user.is_authenticated:
        return redirect('loginclient')

    prestation = prestationForm(request.POST)
    if request.method == 'POST':
        user = request.user
        prestation = prestationForm(request.POST)
        if prestation.is_valid():
            c = prestation.save(commit=False)
            c.client = user
            c.save()
            messages.error(request,"Votre demande a été bien envoyé, s'il vous plait veuillez patienter le temps que vous serez contacter par un professionnel")
            return redirect('/prestation')
        else:
            return render(request,'prestation.html', {'prestation': prestation})
    else:
        prestation = prestationForm()
        return render(request,'prestation.html', {'prestation': prestation})
#-----------------------------------------------------------------------------------------------------------------------
def Compte_Client(request):
    if not request.user.is_authenticated:
        return redirect('loginclient')
    else:
        if request.method == 'POST':
            category = specialitform(request.POST)
            if category.is_valid():
                c = request.POST['specialite']
                category.save()
                return render(request, 'CompteClient.html', {"category": specialitform(),
                                                             "liste_prestataire": prestataire.objects.filter(
                                                                 Specialite=c)})

        else:
            return render(request, 'CompteClient.html',
                          {"category": specialitform(), "liste_prestataire": prestataire.objects.filter()})
                #return redirect('/Compte_Client')
                #c=request.POST['specialite']
                #c.save()

        #return render(request, 'CompteClient.html', {"category":specialitform(),"liste_prestataire": prestataire.objects.filter(Specialite=c)})
#-------------------------------------------------------------------------------------------------------------------------------
def vue_profil(request):
    if not request.user.is_authenticated:
        return redirect('loginprestataire')

    else:
        user = request.user
        pub = publicationForm(request.POST, request.FILES)
        fm = imageForm()


        if request.method == 'POST':
            pub = publicationForm(request.POST, request.FILES)
            fm = imageForm(request.POST, request.FILES)

            files = request.FILES.getlist('photos')
            if pub.is_valid() and fm.is_valid():
                c = pub.save(commit=False)
                c.prestataire = user
                c.save()

                for f in files:
                    gallary = image_publication(photos=f, publication=c)
                    gallary.save()

                pub = publicationForm()
                img = image_publication.objects.filter(publication=c)
                #img = image_publication.objects.filter(publication=c)
                return redirect('vue_profil')
        else:

            pub = publicationForm()
            img = image_publication.objects.filter()
        return render(request, 'Vue profile.html', {'image': img,'form': fm, 'pub': pub,
                                                    "liste_pub": publication.objects.filter(prestataire=user).order_by(
                                                        '-Date_pub')})


#------------------------------------------------------------------------------------------------------------------------
class add_pub(UpdateView):
    model=publication
    class_form=publicationForm()
    template_name = "Vue profile.html"
    success_url = "vue_profil"

#-------------------------------------------------------------------------------------------------------------------------------
def index(request):
    form = loginForm()
    category = specialitform(request.POST)

    if request.method == 'POST':
        form = loginForm(request.POST)
        category = specialitform(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.last_name == "C":
                        return redirect('Compte_Client')
                    elif user.last_name == "P":
                        return redirect('vue_profil')
                else:
                    return HttpResponse('Desolé ce compte n\'existe pas')

            else:
                return HttpResponse('Invalid login')
        elif category.is_valid():
            c = request.POST['specialite']
            category.save()
            return render(request, 'index.html', {"category": specialitform(), "form": loginForm(),
                                                  "liste_prestataire": prestataire.objects.filter(
                                                      Specialite=c)})
    else:
        return render(request, 'index.html', {'form': loginForm(), "category": specialitform(),
                                              "liste_prestataire": prestataire.objects.filter()})
#----------------------------------------------------------------------------------------------

def A_propos(request):
    return render(request, 'About.html', {})

def payement(request):
    return render(request, 'payement.html', {})


def detail_profile(request,id_prestataire):
    """user = request.user
    publi_id=request.publication
    if request.method == 'POST':
        commentaire = commentaireform(request.POST)
        if commentaire.is_valid():
            c = commentaire.save(commit=False)
            c.client = user
            c.publi=publication
            c.save()
            return redirect('/detail_profile')
    else:
        commentaire = commentaireform(request.POST)"""
    prestatair=prestataire.objects.get(user_id=id_prestataire)
    publi=publication.objects.filter(prestataire=id_prestataire).order_by('-Date_pub')
    return render(request, 'detail_profile.html', {'prestataire':prestatair,'liste_pub':publi,'commentaire':commentaire})

#----------------------------------------------------------------------------------------------------------------------------------

"""def commentaire(request,client_id):
    if not request.user.is_authenticated:
        return redirect('loginprestataire')

    else:
        user=request.user
        if request.method == 'POST':
            commentaire = commentaireform(request.POST)
            if commentaire.is_valid():
                c=commentaire.save(commit=False)
                c.prestataire=user
                c.save()
                return redirect('/vue_profil')
        else:
            pub = publicationForm()
        return render(request, 'Vue profile.html', {'pub': pub,"liste_pub": publication.objects.filter(prestataire=user).order_by('-Date_pub')})"""

"""def Login(request):
    form=loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.last_name=="C":
                        return redirect('Compte_Client')
                    elif user.last_name=="P":
                        return redirect('vue_profil')
                else:
                    return HttpResponse('Desolé ce compte n\'existe pas' )

            else:
                return HttpResponse('Invalid login')

    else:
        form=loginForm()
        return render(request,'loggin_appclient.html',{'form':form})"""
