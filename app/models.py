from django.db import models

# Create your models here.
class Imagem(models.Model):
    img = models.FileField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url
    
    
class Obras(models.Model):
    
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=25)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    observacao = models.CharField(max_length=255)
    data_inicio = models.DateField(auto_now=False)
    data_prevista = models.DateField(auto_now=False)
    imagens = models.ManyToManyField(Imagem)
