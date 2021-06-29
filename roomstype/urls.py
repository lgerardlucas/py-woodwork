from django.urls import path
from .views import list_roomstype, new_roomstype, delete_roomstype, edit_roomstype

app_name = 'roomstype'

urlpatterns = [
    path('list/', list_roomstype, name='list_roomstype'),
    path('new/', new_roomstype, name='new_roomstype'),
    path('delete/<int:id>', delete_roomstype, name='delete_roomstype'),
    path('edit/<int:id>', edit_roomstype, name='edit_roomstype'),

]