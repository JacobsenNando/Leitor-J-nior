from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)

    class Meta:
        verbose_name = "livro"

    def __str__(self):
        return self.titulo
