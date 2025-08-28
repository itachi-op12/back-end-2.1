from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    
    return render(request, 'usuario/cadastrar.html')

    # paa front: returne render(request, 'usurio/cadastrar.html')
def login (request):
    return render(request, 'usuario/login.html')    

def logout (request):
    return render(request, 'usuario/logout.html')

def atualizar (request):
    pass

def exibir (request):
    pass

def excluir (request):
    pass

