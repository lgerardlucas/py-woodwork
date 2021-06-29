from django.shortcuts import render, redirect, get_object_or_404
from .models import HomeType
from .forms import HomeTypeForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize

app_name = 'hometype'

def list_hometype(request):
    template_name = 'list_hometype.html'
    hometypes = HomeType.objects.all()

    context = {
        'title_scope':'Imóveis - Listar',
        'records':hometypes,
    }
    return render(request, template_name, context)

def new_hometype(request):
    template_name = 'new_hometype.html'
    form = HomeTypeForm(request.POST or None)
    if form.is_valid():
        home = form.save(commit=False)
        home.name = normalize(home.name.title())
        home.save()
        return redirect('hometype:list_hometype')
    else:
        messages.add_message(request, messages.INFO, form.errors)

    context = {
        'title_scope':'Imóveis - Incluir',
        'records':form,
    }
    return render(request, template_name, context)

def delete_hometype(request, id):
    hometype = HomeType.objects.filter(id=id)
    if hometype:
        hometype.delete()
    return redirect('hometype:list_hometype')

def edit_hometype(request, id):
    template_name = 'edit_hometype.html'
    hometype = HomeType.objects.get(pk=id)
    form = HomeTypeForm(request.POST, instance=hometype)
    if request.method == 'POST':
        if form.is_valid():
            home = form.save(commit=False)
            home.name = normalize(home.name.title())
            home.save()
        return redirect('hometype:list_hometype')
    else:
        context = {
            'title_scope':'Imóveis - Alterar',
            'record':hometype,
        }
        return render(request, template_name, context)
