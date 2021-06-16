from django.urls import path
from .views import new_hometype

app_name = 'hometype'

urlpatterns = [
    path('new/', new_hometype, name='new_hometype'),

]