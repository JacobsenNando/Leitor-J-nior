from django.shortcuts import render
from django.http import HttpResponse
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
        """#return HttpResponse(f'{filtro}')
        if filtro == 1:
            return HttpResponse('1')
        elif filtro == 2:
            return HttpResponse('2')
        elif filtro == 3:
            return HttpResponse('3')
        else:
            return HttpResponse('fail')"""
        #usar **kwargss

        kw = {filtro:busca}

        resultado = Livros.objects.filter(**kw)
        return HttpResponse(f'{resultado[0].titulo}')
        return render(request, 'homepage.html')