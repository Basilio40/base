from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('obras/', views.obras, name='obras'),
    path('documentacao/<int:id>', views.documentacao_1, name='documentacao-1'),
    path('documentacao/categorias/', views.documentacao_categorias, name='documentacao-categorias'),
    path('criar_obra/',views.criar_obra, name='criar_obra'),
    path('upload/', views.upload, name='upload'),
    #projetos
    path('projetos/<str:id>', views.projetos, name='projetos'),
    path('arquitetonico/<str:id>', views.arquitetonico, name='arquitetonico'),
    path('planta_baixa/<str:id>',views.planta_baixa, name='planta_baixa'),
    path('estrutural/<str:id>', views.estrutural, name='estrutural'),
    path('hidraulico/<str:id>', views.hidraulico, name='hidraulico'),
    path('eletrico/<str:id>', views.eletrico, name='eletrico'),
    path('excepcionais/<str:id>', views.excepcionais, name='excepcionais'),
    #Laudo
    path('laudos/<str:id>', views.laudos, name='laudos'),
    path('preliminar/<str:id>', views.preliminar, name='preliminar'),
    path('aterramento/<str:id>', views.aterramento, name='aterramento'),
    path('sondagem/<str:id>', views.sondagem, name='sondagem'),
    path('arrancamento/<str:id>', views.arrancamento, name='arrancamento'),
    path('estanqueidade/<str:id>', views.estanqueidade, name='estanqueidade'),
    path('corpo_prova/<str:id>', views.corpo_prova, name='corpo_prova'),
    #Escopo
    path('escopo/<str:id>', views.escopo, name='escopo'),
    path('serem_executados/<str:id>', views.serem_executados, name='serem_executados'),
    path('obrigacoes/<str:id>', views.obrigacoes, name='obrigacoes'),
    #Contratos
    path('contratos/<str:id>', views.contratos, name='contratos'),
    path('construtora_cliente/<str:id>', views.construtora_cliente, name='construtora_cliente'),
    path('construtora_terceiro/<str:id>', views.construtora_terceiro, name='construtora_terceiro'),
    path('construtora_fornecedor/<str:id>', views.construtora_fornecedor, name='construtora_fornecedor'),
    #Cronograma
    path('cronogramas/<str:id>', views.cronogramas, name='cronogramas'),
    path('fisico_financeiro/<str:id>', views.fisico_financeiro, name='fisico_financeiro'),
    path('fisico/<str:id>', views.fisico, name='fisico'),
    path('financeiro/<str:id>', views.financeiro, name='financeiro'),
    path('notificacoes/<str:id>', views.notificacoes, name='notificacoes'),
    #Compras
    path('compras/<str:id>', views.compras, name='compras'),
    path('solicitacao_de_compras/<str:id>', views.solicitacao_de_compras, name='solicitacao_de_compras'),
    path('cadernos_tecnicos/<str:id>', views.cadernos_tecnicos, name='cadernos_tecnicos'),
    path('termos_garantia/<str:id>', views.termos_garantia, name='termos_garantia'),
    path('memorial_calculo/<str:id>', views.memorial_calculo, name='memorial_calculo'),
    path('logistica/<str:id>', views.logistica, name='logistica'),
    path('historico/<str:id>', views.historico, name='historico'),
    path('tabela_preco/<str:id>', views.tabela_preco, name='tabela_preco'),
    path('romaneio/<str:id>', views.romaneio, name='romaneio'),
    path('status_compra/<str:id>', views.status_compra, name='status_compra'),
    #Serviços
    path('servicos/<str:id>', views.servicos, name='servicos'),
    path('instrucao_tecnica/<str:id>', views.instrucao_tecnica, name='instrucao_tecnica'),
    path('ficha_verificacao/<str:id>', views.ficha_verificacao, name='ficha_verificacao'),
    path('indicador_produtividade/<str:id>', views.indicador_produtividade, name='indicador_produtividade'),
    path('previsao/<str:id>', views.previsao, name='previsao'),
    path('checklist_visita/<str:id>', views.checklist_visita, name='checklist_visita'),
    path('plano_macro/<str:id>', views.plano_macro, name='plano_macro'),
    path('plano_micro/<str:id>', views.plano_micro, name='plano_micro'),
    #Portifolio
    path('portifolio/<str:id>', views.portifolio, name='portifolio'),
    path('fotos/<str:id>', views.fotos, name='fotos'),
    path('videos/<str:id>', views.videos, name='videos'),
    path('informacoes_contato/<str:id>', views.informacoes_contato, name='informacoes_contato'),
   
    
    
    path('sair/', views.sair, name="sair"),
    
]
