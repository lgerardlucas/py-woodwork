from django.urls import path
from .views import list_texturetype, new_texturetype, delete_texturetype, edit_texturetype

app_name = 'texturetype'

urlpatterns = [
    path('list/', list_texturetype, name='list_texturetype'),
    path('new/', new_texturetype, name='new_texturetype'),
    path('delete/<int:id>', delete_texturetype, name='delete_texturetype'),
    path('edit/<int:id>', edit_texturetype, name='edit_texturetype'),

]