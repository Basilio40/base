from django.db import models
from datetime import datetime

# Create your models here.

    
    
class Obras(models.Model):
    
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=25, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField( null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    data_inicio = models.DateField(auto_now=False, null=True, blank=True)
    data_prevista = models.DateField(auto_now=False, null=True, blank=True)
    # Arquitetonico

    
    def data_formatada(self):
        date = datetime.strptime(str(self.data_inicio), '%d-%m-%Y')
        return date
    
    def __str__(self):
        return self.nome
    
    #Planta
class Imagem(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)

#Cortes
class ImageCortes(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
#Layout
#Planta de Cobertura
#Fachada
#Implantação
#Paginação de Piso
#Memorial Descritivo
#Quantitativos
# Fachada


    # Estrutural
#Locação de Infraestrutura
#Infraestrutura
#Superestrutura
#Contenções
#Complementos
#Quantitativos

    #Hidraulico
#Água Fria
#Água Quente
#Pluvial
#Esgoto
#Drenagem
#Infraestrutura
#Reuso/Cisterna

    #Eletrico
#TUG
#TUE
#Alimentação
#Infraestrutura
#SPDA
#Iluminação
#Dados

    #Excepcionais
#Incêndio
#Gás
#Biodigestor
#Impermeabilização
#Comunicação Visual
#Pavimentação
#Jardinagem

    
        # Laudos
    # Preliminar/Cautelar
#Vizinhança
#Uso de Terreno
    #Aterramento
#Teste de Continuidade   
    #Sondagem Solo
#SPT
    # Arrancamento
#Reboco
#Cerâmica
#Chumbadores

    # Estanqueidade
#Caixa D'Água
#Piscina
#Ramais de Esgoto
#Ramal de Água Fria
#Ramal de Ar Pressurizado

    # Corpos de Prova
#Argamassa P/ Alvenaria Estrutural
#Corpos de Prova
#Asfalto

    # Escopo
    # Serviço a serem executados

    # Obrigações

    # Contratos

    #Cronogramas

    #Compras

    #Seviços

    # Portifolio

    




    

    