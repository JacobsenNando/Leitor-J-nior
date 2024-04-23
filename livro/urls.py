from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("search/", views.search, name='search'),
    path("ver_livro/<int:id>", views.ver_livro, name='ver_livro'),
    #path("search/<int:page>", views.search, name='search_paginated'),  # Adiciona a URL para paginação
]
