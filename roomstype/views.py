from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomsType
from .forms import RoomsTypeForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize

app_name = 'roomstype'

def list_roomstype(request):
    template_name = 'list_roomstype.html'
    roomstypes = RoomsType.objects.all()

    context = {
        'title_scope':'Ambientes - Listar',
        'records':roomstypes,
    }
    return render(request, template_name, context)

def new_roomstype(request):
    template_name = 'new_roomstype.html'
    form = RoomsTypeForm(request.POST or None)
    if form.is_valid():
        try:
            room = form.save(commit=False)
            room.name = normalize(room.name.title())
            room.save()
        except IntegrityError as e:
            if 'UNIQUE' in str(e).upper():
                messages.add_message(request, messages.INFO, 'Ambiente "'+room.name+'" já cadastrado!')
            else:
                messages.add_message(request, messages.INFO, 'Erro ao incluir o ambiente "'+room.name+'! '+str(e))
            return redirect('roomstype:new_roomstype')
        return redirect('roomstype:list_roomstype')
    else:
        messages.add_message(request, messages.INFO, form.errors)

    context = {
        'title_scope':'Ambientes - Incluir',
        'records':form,
    }
    return render(request, template_name, context)

def delete_roomstype(request, id):
    roomtype = RoomsType.objects.filter(id=id)
    if roomtype:
        roomtype.delete()
    return redirect('roomstype:list_roomstype')

def edit_roomstype(request, id):
    template_name = 'edit_roomstype.html'
    roomtype = RoomsType.objects.get(pk=id)
    form = RoomsTypeForm(request.POST, instance=roomtype)
    if request.method == 'POST':
        if form.is_valid():
            try:
                room = form.save(commit=False)
                room.name = normalize(room.name.title())
                room.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, 'Ambiente "'+room.name+'" já cadastrado!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir o ambiente "'+room.name+'! '+str(e))
                return redirect('roomstype:new_roomstype')
        return redirect('roomstype:list_roomstype')
    else:
        context = {
            'title_scope':'Ambientes - Alterar',
            'record':roomtype,
        }
        return render(request, template_name, context)
