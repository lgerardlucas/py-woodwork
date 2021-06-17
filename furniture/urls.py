from django.urls import path
from .views import new_furniture

app_name = 'furniture'

urlpatterns = [
    path('new/', new_furniture, name='new_furniture'),

]