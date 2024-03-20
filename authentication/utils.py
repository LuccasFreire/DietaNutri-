import re
from django.contrib import messages
from django.contrib.messages import constants

#VALIDACAO DA SENHA
def senha_e_valida(request, senha):
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no minimo 6 caracteres!')
        return False
    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas!')
        return False
    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minusculas!')
        return False
    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem números!')
        return False

    return True
