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
class ImageLayout(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Planta de Cobertura
class Imagepcobertura(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Fachada
class ImageFachada(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Implantação
class ImageImplantacao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Paginação de Piso
class ImagePaginacao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Memorial Descritivo
class Imagemd(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Quantitativos
class ImageQuantitativo(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
# Fachada
class ImageFachada(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)

    # Estrutural
#Infraestrutura
class ImageInfraestrutura(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Locação de Infraestrutura
class ImageLocinfra(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Superestrutura
class ImageSuperestrutura(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Contenções
class ImageContencoes(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Complementos
class ImageComplementos(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Quantitativos
class ImageQuantitativo(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    #Hidraulico
#Água Fria
class ImageAguafria(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Água Quente
class ImageAguaquente(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Pluvial
class ImagePluvial(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Esgoto
class ImageEsgoto(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Drenagem
class ImageDrenagem(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Infraestrutura
class ImageInfrahidra(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Reuso/Cisterna
class ImageReuso(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Eletrico
#TUG
class ImageTUG(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#TUE
class ImageTUE(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Alimentação
class ImageAlimentacao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Infraestrutura

#SPDA
class ImageSPDA(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Iluminação
class ImageIluminacao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Dados
class ImageDados(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    #Excepcionais
#Incêndio
class ImageIncendio(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Gás
class ImageGas(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Biodigestor
class ImageBiodigestor(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Impermeabilização
class ImageImpermeab(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Comunicação Visual
class ImageComunicacao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Pavimentação
class ImagePavimentacao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Jardinagem
class ImageJardinagem(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    
        # Laudos
    # Preliminar/Cautelar
#Vizinhança
#Uso de Terreno
    #Aterramento
#Teste de Continuidade
class ImageContinuidade(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
      
    #Sondagem Solo
#SPT
class ImageSPT(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    # Arrancamento
#Reboco
class ImageReboco(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Cerâmica
class ImageCeramica(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Chumbadores
class ImageChumbadores(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    # Estanqueidade
#Caixa D'Água
class ImageCaixa(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Piscina
class ImagePiscina(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Ramais de Esgoto
class ImageEsgoto(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Ramal de Água Fria
class ImageRamal_agua(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Ramal de Ar Pressurizado
class ImageRamal_ar(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    # Corpos de Prova
#Argamassa P/ Alvenaria Estrutural
class ImageArgamassa(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Corpos de Prova
class Imagecp(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Asfalto
class ImageAsfalto(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

        # Escopo
    # Serviço a serem executados
#Execução
class ImageExecucao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Compras
class ImageSol_compras(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Contratações
class ImageContratacoes(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#ADM
class ImageAdm(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    # Obrigações
#Pré-Venda
class ImagePrevenda(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Pós-Venda
class ImagePosvenda(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
        # Contratos
    #Pós-Venda Construtora Vs Cliente
class ImageConstrutoracliente(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Somente Cliente e Gerência
    #Construtora Vs 3°S
class ImageConstrutora3(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#Eng Residente e Gerência
    #Construtora Vs Fornecedores
class ImageConstrutoraforn(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

#Eng Residente e Gerência


        #Cronogramas
    #Físico-Financeiro (Desembolso Vs Andamento)
class ImageFisicofinanc(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#
    #Físico
class ImageFisico(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#   
    #Financeiro
class ImageFinanceiro(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
#
    #Notificação de Atrasos
class ImageNotificacoesatrazo(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

        #Compras
    #Solicitação de Compras
class ImageSol_compras(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Cadernos Técnicos
class ImageCaderno(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Termos de Garantia
class ImageTermos(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Memorial de Cálculo
class ImageMemorial(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Logística
class ImageLogistica(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Histórico de Compras
class ImageHistorico(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Tabela de Preços
class ImageTabelaprecos(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Romaneio
class ImageRomaneio(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Status de Compra
class ImageStatus(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

        #Seviços
    #Instrução Técnica de Serviços
class ImageInstrucao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Ficha de Verificação de Serviços
class ImageFicha(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Indicador de Produtividade
class ImageIndicador(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Previsão do Tempo Por Localização Com Histórico
class ImagePrevisao(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    #Checklist Visita Técnica
class ImageChecklist(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    #Plano de Ação Macro
class ImagePlanomacro(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    

    #Plano de Ação Micro
class ImagePlanomicro(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
        # Portifolio
    #Fotos
class ImageFotos(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Vídeos
class ImageVideos(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    
    #Informações Para Contato
class ImageInfcontato(models.Model):
    imagem = models.FileField(upload_to='img',null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    obra = models.ForeignKey(Obras,on_delete=models.CASCADE,null=True, blank=True)
    




    

    