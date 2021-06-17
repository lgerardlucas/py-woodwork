from django.shortcuts import render

# Create your views here.
def new_texturetype(request):
    context = {
        'title':'Tipos de Texturas',
        'about':'Cadastre aqui: Marrocos, Lino, Carvalho, etc...',
    }
    return render(request, 'new_texturetype.html', context)

