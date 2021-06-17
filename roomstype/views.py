from django.shortcuts import render

def new_roomstype(request):
    context = {
        'title':'Tipos de Ambiente',
        'about':'Cadastre aqui: Sala, Quarta, etc...',
    }
    return render(request, 'new_roomstype.html', context)

