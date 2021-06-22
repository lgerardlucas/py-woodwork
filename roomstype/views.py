from django.shortcuts import render

def list_roomstype(request):
    context = {
        'title_scope':'Ambientes',
        'about':'Cadastre aqui: Sala, Quarta, etc...',
    }
    return render(request, 'list_roomstype.html', context)

