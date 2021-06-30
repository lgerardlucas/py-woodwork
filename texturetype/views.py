from django.shortcuts import render, redirect, get_object_or_404
from .models import TextureType
from .forms import TextureTypeForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize

app_name = 'texturetype'

def list_texturetype(request):
    template_name = 'list_texturetype.html'
    texturetypes = TextureType.objects.all()

    context = {
        'title_scope':'Textures - Listar',
        'records':texturetypes,
    }
    return render(request, template_name, context)

def new_texturetype(request):
    template_name = 'new_texturetype.html'
    form = TextureTypeForm(request.POST or None)
    if form.is_valid():
        try:
            texture = form.save(commit=False)
            texture.name = normalize(texture.name.title())
            texture.save()
        except IntegrityError as e:
            if 'UNIQUE' in str(e).upper():
                messages.add_message(request, messages.INFO, 'Textura "'+texture.name+'" já cadastrada!')
            else:
                messages.add_message(request, messages.INFO, 'Erro ao incluir a texture "'+texture.name+'! '+str(e))
            return redirect('texturetype:new_texturetype')
        return redirect('texturetype:list_texturetype')
    else:
        messages.add_message(request, messages.INFO, form.errors)

    context = {
        'title_scope':'Textures - Incluir',
        'records':form,
    }
    return render(request, template_name, context)

def delete_texturetype(request, id):
    texturetype = TextureType.objects.filter(id=id)
    if texturetype:
        texturetype.delete()
    return redirect('texturetype:list_texturetype')

def edit_texturetype(request, id):
    template_name = 'edit_texturetype.html'
    texturetype = TextureType.objects.get(pk=id)
    form = TextureTypeForm(request.POST, instance=texturetype)
    if request.method == 'POST':
        if form.is_valid():
            try:
                texture = form.save(commit=False)
                texture.name = normalize(texture.name.title())
                texture.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, 'Textura "'+texture.name+'" já cadastrada!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir a textura "'+room.name+'! '+str(e))
                return redirect('texturetype:new_texturetype')
        return redirect('texturetype:list_texturetype')
    else:
        context = {
            'title_scope':'Texture - Alterar',
            'record':texturetype,
        }
        return render(request, template_name, context)
