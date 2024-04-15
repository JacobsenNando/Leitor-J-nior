from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')


#--------------------Cadastro--------------------------

"""
################--Status Cadastro--##################
                                                    #
0 = Cadastro realizado com sucesso                  #
1 = Falha no cadastro, nome ou email em branco      #
2 = Falha no cadastro, senha menor que 8 caracteres #
3 = Falha no cadastro, email já cadastrado          #
4 = Erro ao realizar cadastro                       #
                                                    #
#####################################################
""" 

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

  

    usuario = Usuario.objects.filter(email = email)
    
    #---Verificações
    if len(nome.strip())  == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    #---Salva no BD
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, 
                          senha = senha, 
                          email = email)
        usuario.save()

        return redirect('/auth/login/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')
    
#--------------------Login-----------------------------

"""
#################--Status Login--####################
                                                    #
0 = Cadastro realizado com sucesso                  #
1 = Falha no login, email não cadastrado            #
2 = Falha ao acessar pafina, usuário não logado     #
3 =                                                 #
4 =                                                 #
                                                    #
#####################################################
""" 

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    #return HttpResponse(f'{email} {senha}')

    senha = sha256(senha.encode()).hexdigest()

    #Busca usuário que coincide com email e senha
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    #return HttpResponse(f'{usuario[0].email} {usuario[0].senha} {usuario[0].id}')
    
    #Verifica se há usuario conforme email e senha passado, se sim, cria uma session com o id do usuario
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/home/') #?id_usuario={request.session["usuario"]}

#---------------------Logout--------------------------
#Limpa session para fazer logout do usuário do sistema
def logout(request):
    request.session.flush()
    return redirect('/auth/login/')