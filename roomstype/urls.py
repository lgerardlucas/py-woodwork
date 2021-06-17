from django.urls import path
from .views import new_roomstype

app_name = 'roomstype'

urlpatterns = [
    path('new/', new_roomstype, name='new_roomstype'),

]