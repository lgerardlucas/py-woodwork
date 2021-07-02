from django.shortcuts import render, redirect, get_object_or_404
from .models import Furniture
from .forms import FurnitureForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize

app_name = 'furniture'

def list_furniture(request):
    template_name = 'list_furniture.html'
    furnitures = Furniture.objects.all()

    context = {
        'title_scope':'Móveis - Listar',
        'records':furnitures,
    }
    return render(request, template_name, context)

def new_furniture(request):
    template_name = 'new_furniture.html'
    form = FurnitureForm(request.POST or None)
    if form.is_valid():
        try:
            furniture = form.save(commit=False)
            furniture.name = normalize(furniture.name.title())
            furniture.save()
        except IntegrityError as e:
            if 'UNIQUE' in str(e).upper():
                messages.add_message(request, messages.INFO, 'Imóvel "'+furniture.name+'" já cadastrado!')
            else:
                messages.add_message(request, messages.INFO, 'Erro ao incluir o imóvel "'+furniture.name+'! '+str(e))
            return redirect('furniture:new_furniture')
        return redirect('furniture:list_furniture')
    else:
        messages.add_message(request, messages.INFO, form.errors)

    context = {
        'title_scope':'Móveis - Incluir',
        'records':form,
    }
    return render(request, template_name, context)

def delete_furniture(request, id):
    furniture = Furniture.objects.filter(id=id)
    if furniture:
        furniture.delete()
    return redirect('furniture:list_furniture')

def edit_furniture(request, id):
    template_name = 'edit_furniture.html'
    furniture = Furniture.objects.get(pk=id)
    form = FurnitureForm(request.POST, instance=furniture)
    if request.method == 'POST':
        if form.is_valid():
            try:
                home = form.save(commit=False)
                home.name = normalize(home.name.title())
                home.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, 'Imóvel "'+home.name+'" já cadastrado!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir o imóvel "'+home.name+'! '+str(e))
                return redirect('furniture:new_furniture')
        return redirect('furniture:list_furniture')
    else:
        context = {
            'title_scope':'Imóveis - Alterar',
            'record':furniture,
        }
        return render(request, template_name, context)
