from django.shortcuts import render
from django.http import HttpResponse
from .utils import senha_e_valida
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not senha_e_valida(request, senha):
            return redirect('/auth/cadastro')
        try:
            user = User.objects.create_user(username=usuario, email=email, password=senha, is_active=False)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')
        
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = auth.authenticate(username = usuario, password = senha)
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/')
