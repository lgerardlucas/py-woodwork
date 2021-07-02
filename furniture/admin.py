from django.contrib import admin
from .models import Furniture

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)

admin.site.register(Furniture,FurnitureAdmin)