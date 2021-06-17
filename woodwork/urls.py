from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('hometype.urls')),
    path('furniture/', include('furniture.urls')),
    path('rooms/', include('roomstype.urls')),
    path('texture/', include('texturetype.urls')),

]
