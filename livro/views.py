from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from .models import Livros
import re


def home(request):
    if request.session.get("usuario"):
        return render(request, "homepage.html")
        # return HttpResponse('Homepage')
    else:
        return redirect("/auth/login/?status=2")


def search(request):
    if request.session.get("usuario"):
        busca = request.POST.get("search")
        filtro = request.POST.get("filtro")
        re_busca = r"^[a-zA-Z0-9][a-zA-Z0-9\s]*[a-zA-Z0-9]$"  # Regex para validar que que a entrada do usuário é somente uma string alfanumerica sem caracteres especiais
        if re.match(re_busca, busca.strip()):

            if (
                (filtro != "titulo") and (filtro != "autor") and (filtro != "genero")
            ):  # Verifica se não foi adicionado um valor arbitrário pelo usuario em filtros
                return (
                    HttpResponseForbidden()
                )  # Se o valor for difrente dos permitidos retorna 403

                # usando **kwargss
            resultado = Livros.objects.filter(
                **{f"{filtro}__icontains": busca}
            )  # Busca no banco de dados, no atributo passado por "filtro"
            # todos os livros que cujo os quais contenham o valor passado em "busca"
            # sem difrenciar maiúsculas e minusculas(__icontains)
            if len(resultado) == 0:
                return HttpResponse("Nenhum resultado encontrado")
            elif len(resultado) > 0:
                # return HttpResponse(f'{resultado[0].titulo}')
                return render(request, "homepage.html", {"livros": resultado})


def ver_livro(request, id):
    if request.session.get("usuario"):
        livro = Livros.objects.get(id=id)
        # return HttpResponse('ok')
        return render(request, "ver_livro.html", {"livro": livro})
