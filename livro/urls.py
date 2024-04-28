from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("ver_livro/<int:id>", views.ver_livro, name="ver_livro"),
    path("sobre/", views.sobre, name="sobre"),
    
    #urls área administrativa
    path("cadastrar_livro/", views.cadastrar_livro, name='cadastrar_livro'),
    path("valida_cadastro_livro/", views.valida_cadastro_livro, name='valida_cadastro_livro'),
    path("editar_livro/<int:id>", views.editar_livro, name='editar_livro'),
    path("valida_edicao_livro/", views.valida_edicao_livro, name='valida_edicao_livro'),
    path("valida_exclusao_livro/", views.valida_exclusao_livro, name='valida_exclusao_livro'),
    path("search_admin/", views.search_admin, name='search_admin'),
]
