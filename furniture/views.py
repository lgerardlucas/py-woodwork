from django.shortcuts import render



def list_furniture(request):
    context = {
        'title_scope':'Móveis',
        'about':'Cadastre aqui: Roupeiro, Cozinha, etc...',
    }
    return render(request,'list_furniture.html',context)