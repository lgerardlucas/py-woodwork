from django.shortcuts import render

def list_texturetype(request):
    context = {
        'title':'Listas de Texturas',
        'about':'Cadastre aqui: Marrocos, Lino, Carvalho, etc...',
    }
    return render(request, 'list_texturetype.html', context)

