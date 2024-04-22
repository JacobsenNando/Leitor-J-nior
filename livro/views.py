from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from .models import Livros
import re


def home(request):
    if request.session.get("usuario"):
        return render(request, "homepage.html")
    else:
        return redirect("/auth/login/?status=2")


def search(request):
    if request.session.get("usuario"):
        busca = request.POST.get("search")
        filtro = request.POST.get("filtro")
        re_busca = r"^[a-zA-Z0-9][a-zA-Z0-9\s]*[a-zA-Z0-9]$"

        if not re.match(re_busca, busca.strip()):
            return HttpResponseForbidden()

        if filtro not in ["titulo", "autor", "genero"]:
            return HttpResponseForbidden()

        resultado = Livros.objects.filter(**{f"{filtro}__icontains": busca})

        paginator = Paginator(resultado, 20)  # Paginar os resultados, 20 por página
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        if not page_obj.has_next() and page_obj.number != 1:
            return HttpResponseRedirect(
                reverse("search")
                + f"?{request.GET.urlencode()}&page={paginator.num_pages}"
            )

        return render(request, "homepage.html", {"livros": page_obj})


def ver_livro(request, id):
    if request.session.get("usuario"):
        livro = Livros.objects.get(id=id)
        return render(request, "ver_livro.html", {"livro": livro})
