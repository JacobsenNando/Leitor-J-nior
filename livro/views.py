from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from .models import Livros

def  home(request):
    if request.session.get('usuario'):
        return render(request, 'homepage.html')
        #return HttpResponse('Homepage')
    else:
        return redirect('/auth/login/?status=2')


def search(request):
    if request.session.get("usuario"):
        busca = request.POST.get('search')
        filtro = request.POST.get('filtro')
        
        if (filtro != 'titulo') and (filtro !='autor') and (filtro !='genero') :#Verifica se não foi adicionado um valor arbitrario pelo usuario em filtros
            return HttpResponseForbidden() #Se o valor for difrente dos permitidos retorna 403
        
                                                #usando **kwargss
        resultado = Livros.objects.filter(**{f'{filtro}__icontains':busca}) #Busca no banco de dados, no atributo passado por "filtro" 
                                                                            #todos os livros que cujo os quais contenham o valor passado em "busca"
                                                                            #sem difrenciar maiúsculas e minusculas(__icontains)
        if len(resultado) == 0:
            return HttpResponse('Nenhum resultado correspondente')
        elif len(resultado) > 0:
            #return HttpResponse(f'{resultado[0].titulo}')
            return render(request, 'homepage.html', {'livros' : resultado})