from django.contrib import admin
from .models import RoomsType

class RoomsTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)

admin.site.register(RoomsType,RoomsTypeAdmin)