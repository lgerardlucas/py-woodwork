from django.urls import path
from .views import list_furniture, new_furniture, delete_furniture, edit_furniture

app_name = 'furniture'

urlpatterns = [
    path('list/', list_furniture, name='list_furniture'),
    path('new/', new_furniture, name='new_furniture'),
    path('delete/<int:id>', delete_furniture, name='delete_furniture'),
    path('edit/<int:id>', edit_furniture, name='edit_furniture'),

]