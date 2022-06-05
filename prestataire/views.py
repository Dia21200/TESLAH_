from django.contrib.auth import authenticate, login, logout
from . models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  # Redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterprestataireForm, prestataireForm, prestataire_loginForm
from teslahapp.formulaire import loginForm


def Inscrip_prestataire(request):
    if request.method == 'POST':
        user_prestataire_form = RegisterprestataireForm(request.POST)
        prestataire_Form = prestataireForm(request.POST, request.FILES)

        if user_prestataire_form.is_valid() and prestataire_Form.is_valid():
            user = user_prestataire_form.save(commit=False)
            user.last_name = "P"
            user.save()
            prestataire=prestataire_Form.save(commit=False)
            prestataire.user=user
            prestataire.save()

            return redirect('/loginprestataire')

        else:
            user_prestataire_form = RegisterprestataireForm()
            prestataire_Form = prestataireForm()
            return render(request, 'inscr_pro.html', {'user_prestataire_form': user_prestataire_form,'prestataire_Form':prestataire_Form})
    else:
        user_prestataire_form = RegisterprestataireForm()
        prestataire_Form = prestataireForm()
        return render(request, 'inscr_pro.html', {'user_prestataire_form': user_prestataire_form,'prestataire_Form':prestataire_Form})


def loginprestataire(request):
    form=prestataire_loginForm()
    if request.method == 'POST':
        form = prestataire_loginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']

            user = authenticate(request, username=username, password=password)
            #id = prestataire.objects.all().values_list('user_id')
            #current=request.user.id
           # if current not in id:
            #    return render(request, 'logginprestataire.html', {'form': form,'id':id})

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('vue_profil')
                else:
                    return render(request, 'logginprestataire.html', {'form': form})
            else:
                messages.error(request, "Eurreur d\'authentification")
                return render(request, 'logginprestataire.html', {'form': form})

    else:
        form=prestataire_loginForm()
        return render(request,'logginprestataire.html',{'form':form})

def lougout(request):
    context = {}
    logout(request)
    return redirect('index')
