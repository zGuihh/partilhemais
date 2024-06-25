from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

# - Autenticação de modelos e funções

def registro(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect("login")
        
        
    context = {'registerform':form}
    return render(request, 'registro/register.html', context=context)

def dashboard(request):
    return render(request, 'registro/dashboard.html')



