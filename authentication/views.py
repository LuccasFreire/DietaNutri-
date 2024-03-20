from django.shortcuts import render
from django.http import HttpResponse
from .utils import senha_e_valida
from django.shortcuts import redirect
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
        return HttpResponse('testando')


def login(request):
    return HttpResponse('Esta na pagina login')
