from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Obras
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse


@login_required
def obras(request):
    obras = Obras.objects.all()
    context = {
        'obras': obras
    }
    # return HttpResponse(obras)
    return render(request, 'app/obras.html',context)

@login_required
def documentacao_1(request,id):
    obras = Obras.objects.all()
    context = {
        'obras': obras,
        'id':id
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


def sair(request):
    auth.logout(request)
    return redirect('/')