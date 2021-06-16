from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Still - Imóvel
    path('hometype/', include('hometype.urls')),
]
