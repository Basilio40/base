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
    path('planta_imagens/<str:id>',views.planta_imagens, name='planta_imagens'),
    path('remover_planta/<str:ob>?<str:id>?<str:name>', views.remover_cortes, name="remover_planta"),
    path('cortes/<str:id>',views.cortes, name='cortes'),
    path('corte_imagens/<str:id>',views.corte_imagens, name='corte_imagens'),
    path('remover_cortes/<str:ob>?<str:id>?<str:name>', views.remover_cortes, name="remover_cortes"),
    path('fachada/<str:id>',views.fachada, name='fachada'),
    path('fachada_imagens/<str:id>',views.fachada_imagens, name='fachada'),
    path('implantacao/<str:id>',views.implantacao, name='implantacao'),
    path('implantacao_imagens/<str:id>',views.implantacao_imagens, name='implantacao'),
    path('layout/<str:id>',views.layout, name='layout'),
    path('layout_imagens/<str:id>',views.layout_imagens, name='layout'),
    path('md/<str:id>',views.md, name='md'),
    path('md_imagens/<str:id>',views.md_imagens, name='md'),
    path('paginacao/<str:id>',views.paginacao, name='paginacao'),
    path('paginacao_imagens/<str:id>',views.paginacao_imagens, name='paginacao'),
    path('p_cobertura/<str:id>',views.p_cobertura, name='p_cobertura'),
    path('p_cobertura_imagens/<str:id>',views.p_cobertura_imagens, name='p_cobertura'),
    path('quantitativo/<str:id>',views.quantitativo, name='quantitativo'),
    path('quantitativo_imagens/<str:id>',views.quantitativo_imagens, name='quantitativo'),
    #Eletrico
    path('eletrico/<str:id>', views.eletrico, name='eletrico'),
    path('alimentacao/<str:id>',views.alimentacao, name='alimentacao'),
    path('alimentacao_imagens/<str:id>',views.alimentacao_imagens, name='alimentacao'),
    path('dados/<str:id>',views.dados, name='dados'),
    path('dados_imagens/<str:id>',views.dados_imagens, name='dados'),
    path('iluminacao/<str:id>',views.iluminacao, name='iluminacao'),
    path('iluminacao_imagens/<str:id>',views.iluminacao_imagens, name='iluminacao'),
    path('infraestrutura/<str:id>',views.infraestrutura, name='infraestrutura'),
    path('infraestrutura_imagens/<str:id>',views.infraestrutura_imagens, name='infraestrutura'),
    path('SPDA/<str:id>',views.SPDA, name='SPDA'),
    path('SPDA_imagens/<str:id>',views.SPDA_imagens, name='SPDA'),
    path('TUE/<str:id>',views.TUE, name='TUE'),
    path('TUE_imagens/<str:id>',views.TUE_imagens, name='TUE'),
    path('TUG/<str:id>',views.TUG, name='TUG'),
    path('TUG_imagens/<str:id>',views.TUG_imagens, name='TUG'),

    
    #Estrutural
    path('estrutural/<str:id>', views.estrutural, name='estrutural'),
    path('complementos/<str:id>',views.complementos, name='complementos'),
    path('complementos_imagens/<str:id>',views.complementos_imagens, name='complementos'),
    path('contencoes/<str:id>',views.contencoes, name='contencoes'),
    path('contencoes_imagens/<str:id>',views.contencoes_imagens, name='contencoes'),
    path('loc_infra/<str:id>',views.loc_infra, name='loc_infra'),
    path('loc_infra_imagens/<str:id>',views.loc_infra_imagens, name='loc_infra'),
    path('quantitativos/<str:id>',views.quantitativos, name='quantitativos'),
    path('quantitativo_imagens/<str:id>',views.quantitativo_imagens, name='quantitativo'),
    path('superestrutura/<str:id>',views.superestrutura, name='superestrutura'),
    path('superestrutura_imagens/<str:id>',views.superestrutura_imagens, name='superestrutura'),
    
    
    #Excepcionais
    path('excepcionais/<str:id>', views.excepcionais, name='excepcionais'),
    path('biodigestor/<str:id>',views.biodigestor, name='biodigestor'),
    path('biodigestor_imagens/<str:id>',views.biodigestor_imagens, name='biodigestor'),
    path('comunicacao/<str:id>',views.comunicacao, name='comunicacao'),
    path('comunicacao_imagens/<str:id>',views.comunicacao_imagens, name='comunicacao'),
    path('gas/<str:id>',views.gas, name='gas'),
    path('gas_imagens/<str:id>',views.gas_imagens, name='gas'),
    path('impermeab/<str:id>',views.impermeab, name='impermeab'),
    path('impermeab_imagens/<str:id>',views.impermeab_imagens, name='impermeab'),
    path('incendio/<str:id>',views.incendio, name='incendio'),
    path('incendio_imagens/<str:id>',views.incendio_imagens, name='incendio'),
    path('jardinagem/<str:id>',views.jardinagem, name='jardinagem'),
    path('jardinagem_imagens/<str:id>',views.jardinagem_imagens, name='jardinagem'),
    path('pavimentacao/<str:id>',views.pavimentacao, name='pavimentacao'),
    path('pavimentacao_imagens/<str:id>',views.pavimentacao_imagens, name='pavimentacao'),
    
    

    #Hidraulico
    path('hidraulico/<str:id>', views.hidraulico, name='hidraulico'),
    path('agua_fria/<str:id>',views.agua_fria, name='agua_fria'),
    path('agua_quente/<str:id>',views.agua_quente, name='agua_quente'),
    path('drenagem/<str:id>',views.drenagem, name='drenagem'),
    path('esgoto/<str:id>',views.esgoto, name='esgoto'),
    path('infra_hidra/<str:id>',views.infra_hidra, name='infra_hidra'),
    path('pluvial/<str:id>',views.pluvial, name='pluvial'),
    path('reuso/<str:id>',views.reuso, name='reuso'),
    
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
