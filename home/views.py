from django.shortcuts import render

def home(request):
    context = {
        'title_scope':'WoodWork',
        'about':'Escolha sua opção de menu',
    }
    return render(request,'home.html',context)