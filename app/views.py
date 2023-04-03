from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


@login_required
def obras(request):
    return render(request, 'app/obras.html')

@login_required
def documentacao_1(request):
    return render(request, 'app/documentacao_1.html')

@login_required
def documentacao_2(request):
    return render(request, 'app/documentacao_2.html')

@login_required
def documentacao_3(request):
    return render(request, 'app/documentacao_3.html')

@login_required
def documentacao_categorias(request):
    return render(request, 'app/documentacao_categorias.html')

@login_required
def upload(request):
    return render(request, 'app/upload.html')

@login_required
def projetos(request):
    return render(request, 'app/projetos.html')

def arquitetonico(request):
    return render(request, 'app/arquitetonico.html')

def sair(request):
    auth.logout(request)
    return redirect('/')