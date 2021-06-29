from django.urls import path
from .views import list_hometype, new_hometype, delete_hometype, edit_hometype

app_name = 'hometype'

urlpatterns = [
    path('list/', list_hometype, name='list_hometype'),
    path('new/', new_hometype, name='new_hometype'),
    path('delete/<int:id>', delete_hometype, name='delete_hometype'),
    path('edit/<int:id>', edit_hometype, name='edit_hometype'),

]