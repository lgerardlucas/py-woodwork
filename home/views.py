from django.shortcuts import render

def home(request):
    context = {
        'title':'WoodWork',
        'about':'Escolha sua opção de menu',
    }
    return render(request,'home.html',context)