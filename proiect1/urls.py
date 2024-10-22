from django.contrib import admin 
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicatie/', include('aplicatie.urls')),
    path('', include('aplicatie.urls')),
]
