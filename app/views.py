from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Obras, Imagem
from .forms import ObrasForm,PlantaForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages



@login_required
def obras(request):
    endereco = request.GET.get('endereco')
    nome = request.GET.get('nome')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    obras = Obras.objects.all()
    
    if data_inicial and data_final:
        obras = obras.filter(
        data_inicio__range =[data_inicial ,data_final]
    )
    
    context = {
        'obras': obras,
    }
    # return HttpResponse(obras)
    return render(request, 'app/obras.html',context)

@login_required
def criar_obra(request):
    context = {
        'criar_obra':ObrasForm(),
    }
    if request.method == 'POST':
        form = ObrasForm(request.POST)
        if form.is_valid():
            form.save()
    # return HttpResponse(obras)
    return render(request, 'app/criar_obra.html',context)

@login_required
def documentacao_1(request,id):
    obras = Obras.objects.all()
    detalhes = Obras.objects.filter(id=id)
    context = {
        'obras': obras,
        'id':id,
        'detalhes':detalhes
    }
    return render(request, 'app/documentacao_1.html',context)

@login_required
def documentacao_categorias(request):
    return render(request, 'app/documentacao_categorias.html')

@login_required
def upload(request):
    return render(request, 'app/upload.html')

@login_required
def projetos(request,id):
    return render(request, 'app/projetos.html',{'id':id})

@login_required
def laudos(request,id):
    return render(request, 'app/laudos.html',{'id':id})

@login_required
def escopo(request,id):
    return render(request, 'app/escopo.html',{'id':id})

@login_required
def contratos(request,id):
    return render(request, 'app/contratos.html',{'id':id})

@login_required
def cronogramas(request,id):
    return render(request, 'app/cronogramas.html',{'id':id})

@login_required
def compras(request,id):
    return render(request, 'app/compras.html',{'id':id})

@login_required
def servicos(request,id):
    return render(request, 'app/servicos.html',{'id':id})

@login_required
def portifolio(request,id):
    return render(request, 'app/portifolio.html',{'id':id})

#Projetos
def arquitetonico(request,id):
    arquitetonico = Obras.objects.filter(id=id)
    context = {
        'arquitetonico':arquitetonico,
        'id':id
    }
    return render(request, 'app/arquitetonico.html',context)

def planta_baixa(request,id):
    obra = Obras.objects.filter(id=id)
    obra = get_object_or_404(Obras, id=id)
    planta = Obras.objects.filter(id=id)

    context = {
        'planta_f':PlantaForm(),
        'planta':planta,
        'id':id
    }
    if request.method == "GET":
        return render(request,'app/planta_baixa.html',context)
    
    elif request.method == "POST":
        descricao = request.POST.getlist('descricao')
        data = request.POST.getlist('data')

        for n in range(0, len(data)):
            for imagem_upload in request.FILES.getlist('imagem' + str(n)):
                
                imagem = Imagem()
                imagem.imagem = imagem_upload
                imagem.data = data[n]
                imagem.descricao = descricao[n]
                imagem.obra_id = id;
                imagem.save()
            

                
            
    return render(request,'app/planta_baixa.html',context )
    # if request.method == 'POST':
    #     planta = Obras.objects.get(id=id)
    #     formulario = PlantaForm(request.POST, instance=planta)
    #     if formulario.is_valid():
    #         formulario.save()
            
    # return render(request,'app/planta_baixa.html',context )

def planta_imagens(request,id):
    planta = Obras.objects.filter(id=id)
    obra = get_object_or_404(Obras, id=id)
    data_inicial = request.GET.get('data_inicial')
    if data_inicial:
        planta = planta.filter(planta_data=data_inicial)
    context = {
        'planta':planta,
        'id':id
    }


    # EDITAR
    if request.method == "POST":
        editar_descricao = request.POST.get('editar_descricao')
        for item in imagens:
            item.descricao = editar_descricao
            item.save()
            
    return render(request,'app/planta_imagens.html',context)
    # DELETAR

def remover_planta(request,id,*args,**kwargs):
    planta = Obras.objects.filter(id=id)

    for item in planta:
        deletar = item.imagem_planta_baixa
        deletar.delete()
        messages.success(request, "Eliminado com Sucesso")
    return redirect('obras')
        
    

def estrutural(request,id):
    estrutural = Obras.objects.filter(id=id)
    context = {
        'estrutural':estrutural,
        'id':id
    }
    return render(request, 'app/estrutural.html',context)

def hidraulico(request,id):
    hidraulico = Obras.objects.filter(id=id)
    context = {
        'hidraulico':hidraulico,
        'id':id
    }
    return render(request, 'app/hidraulico.html',context)

def eletrico(request,id):
    eletrico = Obras.objects.filter(id=id)
    context = {
        'eletrico':eletrico,
        'id':id
    }
    return render(request, 'app/eletrico.html',context)

def excepcionais(request,id):
    excepcionais = Obras.objects.filter(id=id)
    context = {
        'excepcionais':excepcionais,
        'id':id
    }
    return render(request, 'app/excepcionais.html',context)

# Laudos
def preliminar(request,id):
    preliminar = Obras.objects.filter(id=id)
    context = {
        'preliminar':preliminar,
        'id':id
    }
    return render(request, 'app/preliminar.html',context)

def aterramento(request,id):
    aterramento = Obras.objects.filter(id=id)
    context = {
        'aterramento':aterramento,
        'id':id
    }
    return render(request, 'app/aterramento.html',context)

def sondagem(request,id):
    sondagem = Obras.objects.filter(id=id)
    context = {
        'sondagem':sondagem,
        'id':id
    }
    return render(request, 'app/sondagem.html',context)

def arrancamento(request,id):
    arrancamento = Obras.objects.filter(id=id)
    context = {
        'arrancamento':arrancamento,
        'id':id
    }
    return render(request, 'app/arrancamento.html',context)

def estanqueidade(request,id):
    estanqueidade = Obras.objects.filter(id=id)
    context = {
        'estanqueidade':estanqueidade,
        'id':id
    }
    return render(request, 'app/estanqueidade.html',context)

def corpo_prova(request,id):
    corpo_prova = Obras.objects.filter(id=id)
    context = {
        'corpo_prova':corpo_prova,
        'id':id
    }
    return render(request, 'app/corpo_prova.html',context)

#Escopo
def serem_executados(request,id):
    serem_executados = Obras.objects.filter(id=id)
    context = {
        'serem_executados':serem_executados,
        'id':id
    }
    return render(request, 'app/serem_executados.html',context)

def obrigacoes(request,id):
    obrigacoes = Obras.objects.filter(id=id)
    context = {
        'obrigacoes':obrigacoes,
        'id':id
    }
    return render(request, 'app/obrigacoes.html',context)
#Contratos
def construtora_cliente(request,id):
    construtora_cliente = Obras.objects.filter(id=id)
    context = {
        'construtora_cliente':construtora_cliente,
        'id':id
    }
    return render(request, 'app/construtora_cliente.html',context)

def construtora_terceiro(request,id):
    construtora_terceiro = Obras.objects.filter(id=id)
    context = {
        'construtora_terceiro':construtora_terceiro,
        'id':id
    }
    return render(request, 'app/construtora_terceiro.html',context)

def construtora_fornecedor(request,id):
    construtora_fornecedor = Obras.objects.filter(id=id)
    context = {
        'construtora_fornecedor':construtora_fornecedor,
        'id':id
    }
    return render(request, 'app/construtora_fornecedor.html',context)

#Cronogramas
def fisico_financeiro(request,id):
    fisico_financeiro = Obras.objects.filter(id=id)
    context = {
        'fisico_financeiro':fisico_financeiro,
        'id':id
    }
    return render(request, 'app/fisico_financeiro.html',context)

def fisico(request,id):
    fisico = Obras.objects.filter(id=id)
    context = {
        'fisico':fisico,
        'id':id
    }
    return render(request, 'app/fisico.html',context)

def financeiro(request,id):
    financeiro = Obras.objects.filter(id=id)
    context = {
        'financeiro':financeiro,
        'id':id
    }
    return render(request, 'app/financeiro.html',context)

def notificacoes(request,id):
    notificacoes = Obras.objects.filter(id=id)
    context = {
        'notificacoes':notificacoes,
        'id':id
    }
    return render(request, 'app/notificacoes.html',context)

#Compras

def solicitacao_de_compras(request,id):
    solicitacao_de_compras = Obras.objects.filter(id=id)
    context = {
        'solicitacao_de_compras':solicitacao_de_compras,
        'id':id
    }
    return render(request, 'app/solicitacao_de_compras.html',context)

def cadernos_tecnicos(request,id):
    cadernos_tecnicos = Obras.objects.filter(id=id)
    context = {
        'cadernos_tecnicos':cadernos_tecnicos,
        'id':id
    }
    return render(request, 'app/cadernos_tecnicos.html',context)

def termos_garantia(request,id):
    termos_garantia = Obras.objects.filter(id=id)
    context = {
        'termos_garantia':termos_garantia,
        'id':id
    }
    return render(request, 'app/termos_garantia.html',context)

def memorial_calculo(request,id):
    memorial_calculo = Obras.objects.filter(id=id)
    context = {
        'memorial_calculo':memorial_calculo,
        'id':id
    }
    return render(request, 'app/memorial_calculo.html',context)

def logistica(request,id):
    logistica = Obras.objects.filter(id=id)
    context = {
        'logistica':logistica,
        'id':id
    }
    return render(request, 'app/logistica.html',context)

def historico(request,id):
    historico = Obras.objects.filter(id=id)
    context = {
        'historico':historico,
        'id':id
    }
    return render(request, 'app/historico.html',context)

def tabela_preco(request,id):
    tabela_preco = Obras.objects.filter(id=id)
    context = {
        'tabela_preco':tabela_preco,
        'id':id
    }
    return render(request, 'app/tabela_preco.html',context)

def romaneio(request,id):
    romaneio = Obras.objects.filter(id=id)
    context = {
        'romaneio':romaneio,
        'id':id
    }
    return render(request, 'app/romaneio.html',context)

def status_compra(request,id):
    status_compra = Obras.objects.filter(id=id)
    context = {
        'status_compra':status_compra,
        'id':id
    }
    return render(request, 'app/status_compra.html',context)

#Serviços
def instrucao_tecnica(request,id):
    instrucao_tecnica = Obras.objects.filter(id=id)
    context = {
        'instrucao_tecnica':instrucao_tecnica,
        'id':id
    }
    return render(request, 'app/instrucao_tecnica.html',context)

def ficha_verificacao(request,id):
    ficha_verificacao = Obras.objects.filter(id=id)
    context = {
        'ficha_verificacao':ficha_verificacao,
        'id':id
    }
    return render(request, 'app/ficha_verificacao.html',context)

def indicador_produtividade(request,id):
    indicador_produtividade = Obras.objects.filter(id=id)
    context = {
        'indicador_produtividade':indicador_produtividade,
        'id':id
    }
    return render(request, 'app/indicador_produtividade.html',context)

def previsao(request,id):
    previsao = Obras.objects.filter(id=id)
    context = {
        'previsao':previsao,
        'id':id
    }
    return render(request, 'app/previsao.html',context)

def checklist_visita(request,id):
    checklist_visita = Obras.objects.filter(id=id)
    context = {
        'checklist_visita':checklist_visita,
        'id':id
    }
    return render(request, 'app/checklist_visita.html',context)

def plano_macro(request,id):
    plano_macro = Obras.objects.filter(id=id)
    context = {
        'plano_macro':plano_macro,
        'id':id
    }
    return render(request, 'app/plano_macro.html',context)

def plano_micro(request,id):
    plano_micro = Obras.objects.filter(id=id)
    context = {
        'plano_micro':plano_micro,
        'id':id
    }
    return render(request, 'app/plano_micro.html',context)


#Portifolio
def fotos(request,id):
    fotos = Obras.objects.filter(id=id)
    context = {
        'fotos':fotos,
        'id':id
    }
    return render(request, 'app/fotos.html',context)

def videos(request,id):
    videos = Obras.objects.filter(id=id)
    context = {
        'videos':videos,
        'id':id
    }
    return render(request, 'app/videos.html',context)

def informacoes_contato(request,id):
    informacoes_contato = Obras.objects.filter(id=id)
    context = {
        'informacoes_contato':informacoes_contato,
        'id':id
    }
    return render(request, 'app/informacoes_contato.html',context)


def sair(request):
    auth.logout(request)
    return redirect('/')