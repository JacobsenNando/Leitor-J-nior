from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect

def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request, 'cadastro.html')


#--------------------Cadastro--------------------------

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    

#---Verificações
####################--Status--#######################
"""                                                 #
0 = Cadastro realizado com sucesso                  #
1 = Falha no cadastro, nome ou email em branco      #
2 = Falha no cadastro, senha menor que 8 caracteres #
3 = Falha no cadastro, email já cadastrado          #
4 = Erro ao realizar cadastro                       #
                                                    #
"""                                                 #
#####################################################
    
    usuario = Usuario.objects.filter(email = email)
    
    if len(nome.strip())  == 0 or len(email.strip)) == 0;
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        usuario = Usuario(nome = nome, 
                          senha = senha, 
                        email = email)
        usuario.save()

        return redirect('/auth/login/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')