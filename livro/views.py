from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def  home(request):
    if request.session.get('usuario'):
        return render(request, 'homepage.html')
        #return HttpResponse('Homepage')
    else:
        return redirect('/auth/login/?status=2')

def search(request):
    if request.session.get("usuario"):
        busca = request.POST.get('search')
        filtro = int(request.POST.get('filtro'))
        #return HttpResponse(f'{filtro}')
        if filtro == 1:
            return HttpResponse('1')
        elif filtro == 2:
            return HttpResponse('2')
        elif filtro == 3:
            return HttpResponse('3')
        else:
            return HttpResponse('fail')


        resultado = Livros.objects.filter()
        return render(request, 'homepage.html')