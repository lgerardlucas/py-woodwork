from django.urls import path
from .views import list_hometype

app_name = 'hometype'

urlpatterns = [
    path('list/', list_hometype, name='list_hometype'),
]