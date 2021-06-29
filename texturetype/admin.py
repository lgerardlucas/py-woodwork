from django.contrib import admin
from .models import TextureType

class TextureTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)

admin.site.register(TextureType,TextureTypeAdmin)