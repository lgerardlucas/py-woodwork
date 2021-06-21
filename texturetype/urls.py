from django.urls import path
from .views import list_texturetype

app_name = 'texturetype'

urlpatterns = [
    path('list/', list_texturetype, name='list_texturetype'),

]