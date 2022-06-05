from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  # Redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterclientForm, clientForm, client_loginForm



def Inscrip_client(request):
    if request.method == 'POST':
        user_form = RegisterclientForm(request.POST)
        client_Form = clientForm(request.POST)

        if user_form.is_valid() and client_Form.is_valid():
            user=user_form.save(commit=False)
            user.last_name="C"
            user.save()

            client=client_Form.save(commit=False)
            client.user=user
            client.save()
            messages.success(request, "Merci pour votre inscription!")
            return redirect('/loginclient')

        else:
            user_form = RegisterclientForm()
            client_Form = clientForm()
            return render(request, 'inscrip_appclient.html', {'user_form': user_form,'client_Form':client_Form})
    else:
        user_form = RegisterclientForm()
        client_Form = clientForm()
        return render(request, 'inscrip_appclient.html', {'user_form': user_form,'client_Form':client_Form})


def loginclient(request):
    formc_lient=client_loginForm()
    if request.method == 'POST':
        formc_lient = client_loginForm(request.POST)
        if formc_lient.is_valid():
            username=request.POST['username']
            password=request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.last_name == "C":
                        return redirect('Compte_Client')
                    else:
                        return redirect('loginclient')
                else:
                    return HttpResponse('Desolé ce compte n\'existe pas' )

            else:
                return HttpResponse('Invalid login')

    else:
        formc_lient=client_loginForm()
        return render(request,'loggin_appclient.html',{'formc_lient':formc_lient})


def lougout(request):
    context = {}
    logout(request)
    return redirect('index')

def login_prestation(request):
    formc_lient=client_loginForm()
    if request.method == 'POST':
        formc_lient = client_loginForm(request.POST)
        if formc_lient.is_valid():
            username=request.POST['username']
            password=request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.last_name == "C":
                        return redirect('prestation')
                    else:
                        return redirect('login_prestation')
                else:
                    return HttpResponse('Desolé ce compte n\'existe pas' )

            else:
                return HttpResponse('Desolé ce compte n\'existe pas')

    else:
        formc_lient=client_loginForm()
        return render(request,'loggin_appclient.html',{'formc_lient':formc_lient})
