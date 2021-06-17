from django.urls import path
from .views import new_texturetype

app_name = 'texturetype'

urlpatterns = [
    path('new/', new_texturetype, name='new_texturetype'),

]