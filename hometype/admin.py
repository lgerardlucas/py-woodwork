from django.contrib import admin
from .models import HomeType

class HomeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)

admin.site.register(HomeType,HomeTypeAdmin)