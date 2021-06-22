from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('hometype/', include('hometype.urls')),
    path('furniture/', include('furniture.urls')),
    path('roomstype/', include('roomstype.urls')),
    path('texturetype/', include('texturetype.urls')),

]
