from django.shortcuts import render

# Create your views here.
def new_hometype(request):
    context = {
        'title':'Tipos de Imóveis',
        'about':'Cadastre aqui: Casa, Apartamento, etc...',
    }
    return render(request, 'new_hometype.html', context)

