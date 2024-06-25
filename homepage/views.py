from django.shortcuts import render, redirect
from registro.forms import LoginForm

# - Autenticação de modelos e funções

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'homepage/index.html')

def sobrenos(request):
    return render(request, 'homepage/sobrenos.html')

def termos(request):
    return render(request, 'homepage/termos.html')

def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request,user)

                return redirect("dashboard")
            
    context = {'loginform':form}

    return render(request, 'homepage/login.html', context=context)

def user_logout(request):

    auth.logout(request)

    return redirect("")