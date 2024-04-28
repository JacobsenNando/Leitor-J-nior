from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)

    class Meta:
        verbose_name = "livro"

    def __str__(self):
        return self.titulo
    
class Resumos(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    resumo = models.TextField()
    usuario = models.ForeignKey("usuarios.Usuarios", on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

class Avaliacoes(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    nota = models.IntegerField()
    usuario = models.ForeignKey("usuarios.Usuarios", on_delete=models.CASCADE)