
import os
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Change to ads.urls
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep

    # Sample applications
    path('autos/', include('autos.urls')),
]
