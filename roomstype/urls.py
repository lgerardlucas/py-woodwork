from django.urls import path
from .views import list_roomstype

app_name = 'roomstype'

urlpatterns = [
    path('list/', list_roomstype, name='list_roomstype'),

]