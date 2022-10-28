from django.contrib import admin
from django.urls import path
from clientes import urls as clientes_urls


urlpatterns = [    
    path('clientes/', include(clientes_urls)),
    path('admin/', admin.site.urls),
]
