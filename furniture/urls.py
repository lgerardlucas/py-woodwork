from django.urls import path
from .views import list_furniture

app_name = 'furniture'

urlpatterns = [
    path('list/', list_furniture, name='list_furniture'),

]