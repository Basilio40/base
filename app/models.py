from django.db import models

# Create your models here.
class Imagem(models.Model):
    img = models.FileField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url
    
    
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
    imagens = models.ManyToManyField(Imagem, null=True, blank=True)
    # Arquitetonico
    planta_baixa = models.URLField(max_length=200, null=True, blank=True)
    cortes = models.URLField(max_length=200, null=True, blank=True)
    Layout = models.URLField(max_length=200, null=True, blank=True)
    planta_de_cobertura = models.URLField(max_length=200, null=True, blank=True)
    fachada = models.URLField(max_length=200, null=True, blank=True)
    implantacao = models.URLField(max_length=200, null=True, blank=True)
    paginacao_de_piso = models.URLField(max_length=200, null=True, blank=True)
    memorial_descritivo = models.URLField(max_length=200, null=True, blank=True)
    # Estrutural
    locacao_de_infraestrurura = models.URLField(max_length=200, null=True, blank=True)
    infraestrutura = models.URLField(max_length=200, null=True, blank=True)
    superestrutura = models.URLField(max_length=200, null=True, blank=True)
    contencoes = models.URLField(max_length=200, null=True, blank=True)
    complementos = models.URLField(max_length=200, null=True, blank=True)
    quantitativos = models.URLField(max_length=200, null=True, blank=True)
    #Hidraulico
    agua_fria = models.URLField(max_length=200, null=True, blank=True)
    agua_quente = models.URLField(max_length=200, null=True, blank=True)
    pluvial = models.URLField(max_length=200, null=True, blank=True)
    esgoto = models.URLField(max_length=200, null=True, blank=True)
    drenagem = models.URLField(max_length=200, null=True, blank=True)
    infraestrutura = models.URLField(max_length=200, null=True, blank=True)
    reuso = models.URLField(max_length=200, null=True, blank=True)
    #Eletrico
    TUG = models.URLField(max_length=200, null=True, blank=True)
    TUE = models.URLField(max_length=200, null=True, blank=True)
    alimentacao= models.URLField(max_length=200, null=True, blank=True)
    infraestrutura_eletrica = models.URLField(max_length=200, null=True, blank=True)
    SPDA = models.URLField(max_length=200, null=True, blank=True)
    iluminacao = models.URLField(max_length=200, null=True, blank=True)
    dados = models.URLField(max_length=200, null=True, blank=True)
    #Excepcionais
    incendio = models.URLField(max_length=200, null=True, blank=True)
    gas = models.URLField(max_length=200, null=True, blank=True)
    biodigestores = models.URLField(max_length=200, null=True, blank=True)
    impermeabilizacao = models.URLField(max_length=200, null=True, blank=True)
    comunicacao_visual = models.URLField(max_length=200, null=True, blank=True)
    pavimentacao = models.URLField(max_length=200, null=True, blank=True)
    jardinagem = models.URLField(max_length=200, null=True, blank=True)
    
    # Laudos
    # Preliminar/Cautelar
    vizinhanca = models.URLField(max_length=200, null=True, blank=True)
    uso_terreno = models.URLField(max_length=200, null=True, blank=True)
    #Aterramento
    teste_continuidade = models.URLField(max_length=200, null=True, blank=True)
    #Sondagem Solo
    SPT = models.URLField(max_length=200, null=True, blank=True)
    # Arrancamento
    reboco = models.URLField(max_length=200, null=True, blank=True)
    ceramica = models.URLField(max_length=200, null=True, blank=True)
    chumbadores = models.URLField(max_length=200, null=True, blank=True)
    # Estanqueidade
    caixa_dagua = models.URLField(max_length=200, null=True, blank=True)
    piscina = models.URLField(max_length=200, null=True, blank=True)
    ramais_esgoto = models.URLField(max_length=200, null=True, blank=True)
    ramais_agua_fria = models.URLField(max_length=200, null=True, blank=True)
    ramais_ar_pressurizado = models.URLField(max_length=200, null=True, blank=True)
    # Corpos de Prova
    argamassa = models.URLField(max_length=200, null=True, blank=True)
    corpo_de_prova = models.URLField(max_length=200, null=True, blank=True)
    asfalto = models.URLField(max_length=200, null=True, blank=True)
    # Escopo
    # Serviço a serem executados
    execucao = models.URLField(max_length=200, null=True, blank=True)
    compras = models.URLField(max_length=200, null=True, blank=True)
    contratacoes = models.URLField(max_length=200, null=True, blank=True)
    ADM = models.URLField(max_length=200, null=True, blank=True)
    # Obrigações
    pre_venda = models.URLField(max_length=200, null=True, blank=True)
    pos_venda = models.URLField(max_length=200, null=True, blank=True)
    # Contratos
    construtora_cliente = models.URLField(max_length=200, null=True, blank=True)
    construtora_terceiros = models.URLField(max_length=200, null=True, blank=True)
    construtora_fornecedores = models.URLField(max_length=200, null=True, blank=True)
    #Cronogramas
    fisico_financeiro = models.URLField(max_length=200, null=True, blank=True)
    fisico_financeiro1 = models.URLField(max_length=200, null=True, blank=True)
    fisico = models.URLField(max_length=200, null=True, blank=True)
    fisico1 = models.URLField(max_length=200, null=True, blank=True)
    financeiro = models.URLField(max_length=200, null=True, blank=True)
    financeiro1 = models.URLField(max_length=200, null=True, blank=True)
    notificacao = models.URLField(max_length=200, null=True, blank=True) 
    #Compras
    solicitacao_compras = models.URLField(max_length=200, null=True, blank=True)
    caderno_tecnico = models.URLField(max_length=200, null=True, blank=True)
    termos_garantia = models.URLField(max_length=200, null=True, blank=True)
    memorial_calculo = models.URLField(max_length=200, null=True, blank=True)
    logistica = models.URLField(max_length=200, null=True, blank=True)
    historico_compras = models.URLField(max_length=200, null=True, blank=True)
    tabela_de_preco = models.URLField(max_length=200, null=True, blank=True)
    romaneio = models.URLField(max_length=200, null=True, blank=True)
    status_compras = models.URLField(max_length=200, null=True, blank=True)
    #Seviços
    instrucao_tecnica = models.URLField(max_length=200, null=True, blank=True)
    ficha_verificacao = models.URLField(max_length=200, null=True, blank=True)
    indicador_produtividade = models.URLField(max_length=200, null=True, blank=True)
    previsao_tempo = models.URLField(max_length=200, null=True, blank=True)
    checklist_visita_tecnica = models.URLField(max_length=200, null=True, blank=True)
    plano_acao_macro = models.URLField(max_length=200, null=True, blank=True)
    plano_acao_micro = models.URLField(max_length=200, null=True, blank=True)
    # Portifolio
    fotos = models.URLField(max_length=200, null=True, blank=True)
    videos = models.URLField(max_length=200, null=True, blank=True)
    informacoes_contato = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.nome
