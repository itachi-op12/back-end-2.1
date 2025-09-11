from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login')

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # tentar autenticar usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("perfil")
        else:
            messages.error(request, "Usuário ou senha incorretos")
    
    return render(request, "usuario/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if password != password2:
            messages.error(request, "As senhas não conferem")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("perfil")
    
    return render(request, "usuario/registrar.html")

@login_required
def perfil(request):
    return render(request, "usuario/perfil.html", {"usuario": request.user})
