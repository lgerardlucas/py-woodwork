from django.shortcuts import render

# Create your views here.
def list_hometype(request):
    context = {
        'title':'Lista de Imóveis',
        'about':'Cadastre aqui: Casa, Apartamento, etc...',
    }
    return render(request, 'list_hometype.html', context)

