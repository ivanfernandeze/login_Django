from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('seguridad.urls')),
    path('crud/', include('ventasApp.urls')),
    path('crud/', include('comprasApp.urls')),
]
