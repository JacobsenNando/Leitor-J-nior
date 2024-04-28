from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from .models import Livros
from usuarios.models import Usuario
import re
from urllib.parse import urlparse


def home(request):
    if request.session.get("usuario"):
        return render(request, "search_page.html")
    else:
        return redirect("/auth/login/?status=2")


def search(request):
    if request.session.get("usuario"):
        busca = request.GET.get("search")
        filtro = request.GET.get("filtro")
        
        # Verifica se a busca é válida
        re_busca = r"^[a-zA-Z0-9][a-zA-Z0-9\s]*[a-zA-Z0-9]$"

        if not re.match(re_busca, busca.strip()):
            return HttpResponseForbidden()

        if filtro not in ["titulo", "autor", "genero"]:
            return HttpResponseForbidden()

        resultado = Livros.objects.filter(**{f"{filtro}__icontains": busca})

        #Realiza a paginação dos resultados
        paginator = Paginator(resultado, 20)  # Paginar os resultados, 20 por página
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(request, "home_page.html", {"livros": page_obj})

def ver_livro(request, id):
    if request.session.get("usuario"):
        livro = Livros.objects.get(id=id)
        return render(request, "ver_livro.html", {"livro": livro})

############################################################################
#-------------------------Área administrativa------------------------------#
############################################################################
"""
################--Status Cadastro Livro--#################
                                                         #
0 = Cadastro realizado com sucesso                       #
1 = Falha no cadastro, titulo, autor ou genero em branco #
2 = N/A                                                  #
3 = Flaha no cadastro, livro já cadastrado               #
4 = Erro ao realizar cadastro                            #
                                                         #
##########################################################
""" 



def cadastrar_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        return render(request, "cad_livro.html")
    else:
        return HttpResponseForbidden()

def valida_cadastro_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        genero = request.POST.get("genero")

        #xml_body = request.body.decode('utf-8')

        # Analisa o XML
        #root = ET.fromstring(xml_body)

        # Extrai os dados relevantes do XML
        #titulo = root.find('titulo').text
        #autor = root.find('autor').text
        #genero = root.find('genero').text

        livro = Livros.objects.filter(titulo = titulo).filter(autor = autor)

        #---Verificações
        if len(titulo.strip()) == 0 or len(autor.strip()) == 0 or len(genero.strip()) == 0:
            return redirect('/livro/cadastrar_livro/?status=1')
        if len(livro) > 0:
            return redirect('/livro/cadastrar_livro/?status=3')
        
        try:
            livro = Livros(titulo = titulo,
                           autor = autor,
                           genero = genero)
            livro.save()
            return redirect('/livro/cadastrar_livro/?status=0')
        except:
            return redirect('/livro/cadastrar_livro/?status=4')

        
    else:
        return HttpResponseForbidden()
    
def editar_livro(request, id):
    if request.session.get("usuario") and request.session.get("admin"):
        livro = Livros.objects.get(id=id)
        return render(request, "insira_aqui_o_arquivo.html", {"livro": livro})
    
    else:
        return HttpResponseForbidden()


"""
#################--Status Edição Livro--##################
                                                         #
0 = Edição realizada com sucesso                         #
1 = Falha na edição, titulo, autor ou genero em branco   #
2 = N/A                                                  #
3 = Flaha na edição, já existe um livro com estes dados  #
4 = Erro ao editar livro                                 #
                                                         #
##########################################################
""" 
def valida_edicao_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        id = request.POST.get("id")
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        genero = request.POST.get("genero")

        livro = Livros.objects.get(id=id)

        #---Verificações
        if len(titulo.strip()) == 0 or len(autor.strip()) == 0 or len(genero.strip()) == 0: 
            return redirect('/livro/valida_edição_livro/?status=1')
        
        livro_existente = Livros.objects.filter(titulo__iexact = titulo).filter(autor__iexact = autor)
        if len(livro_existente) > 0:
            return redirect('/livro/valida_edição_livro/?status=3')
        
        try:
            livro.titulo = titulo
            livro.autor = autor
            livro.genero = genero
            livro.save()
            return redirect('/livro/valida_edição_livro/?status=0')
        except:
            return redirect('/livro/valida_edição_livro/?status=4')
    else:
        return HttpResponseForbidden()
    

"""
################--Status Exclusão Livro--#################
                                                         #
0 = Exclusão realizada com sucesso                       #
1 = N/A                                                  #
2 = N/A                                                  #
3 = N/A                                                  #
4 = Erro ao editar livro                                 #
                                                         #
##########################################################
""" 

def valida_exclusao_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        id = request.POST.get("id")

        try:
            livro = Livros.objects.get(id=id)
            livro.delete()
            return redirect('/livro/editar_livro/?status=0')
        except:
            return redirect('/livro/editar_livro/?status=4')
    else:
        return HttpResponseForbidden()




def search_admin(request):
        if request.session.get("usuario") and request.session.get("admin"):
            busca = request.GET.get("search")
            filtro = request.GET.get("filtro")
            
            # Verifica se a busca é válida
            re_busca = r"^[a-zA-Z0-9][a-zA-Z0-9\s]*[a-zA-Z0-9]$"

            if not re.match(re_busca, busca.strip()):
                return HttpResponseForbidden()

            if filtro not in ["titulo", "autor", "genero"]:
                return HttpResponseForbidden()

            resultado = Livros.objects.filter(**{f"{filtro}__icontains": busca})

            #Realiza a paginação dos resultados
            paginator = Paginator(resultado, 20)  # Paginar os resultados, 20 por página
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            
            return render(request, "partial_search.html", {"livros": page_obj}) # Verifica se a requisição veio da página de cadastro de livro
        else:
            return HttpResponseForbidden()