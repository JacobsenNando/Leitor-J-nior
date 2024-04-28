from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)

    class Meta:
        verbose_name = "livro"

    def __str__(self):
        return self.titulo
    
class Resenhas(models.Model):
    resenha = models.TextField()
    livro_fk = models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario_fk = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        verbose_name = "resenha"

    def __str__(self):
        return self.titulo

class Avaliacoes(models.Model):
     livro_fk = models.ForeignKey(Livros, on_delete=models.CASCADE)
     nota = models.IntegerField()
     usuario_fk = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
     
     class Meta:
        verbose_name = "avaliacao"

     def __str__(self):
        return self.titulo