from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('obras/', views.obras, name='obras'),
    path('documentacao/<str:id>', views.documentacao_1, name='documentacao-1'),
    path('documentacao/categorias/', views.documentacao_categorias, name='documentacao-categorias'),
    path('upload/', views.upload, name='upload'),
    #projetos
    path('projetos/<str:id>', views.projetos, name='projetos'),
    path('arquitetonico/<str:id>', views.arquitetonico, name='arquitetonico'),
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
    #Contratos
    path('contratos/<str:id>', views.contratos, name='contratos'),
    #Cronograma
    path('cronogramas/<str:id>', views.cronogramas, name='cronogramas'),
    #Compras
    path('compras/<str:id>', views.compras, name='compras'),
    #Serviços
    path('servicos/<str:id>', views.servicos, name='servicos'),
    #Portifolio
    path('portifolio/<str:id>', views.portifolio, name='portifolio'),
   
    
    
    path('sair/', views.sair, name="sair"),
    
]
