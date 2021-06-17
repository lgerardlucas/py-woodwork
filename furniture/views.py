from django.shortcuts import render

def new_furniture(request):
    context = {
        'title':'Cadastro de Móveis',
        'about':'Cadastre aqui: Roupeiro, Cozinha, etc...',
    }
    return render(request,'new_furniture.html',context)