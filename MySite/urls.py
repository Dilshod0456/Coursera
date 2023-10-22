from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('week2', include('week2.urls')),
    path('polls/', include('polls.urls', namespace='polls')),
    path('', include('hello.urls', namespace='hello')),
]
