from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls
from wp import urls as wp_url


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [    
    path('', include(home_urls)),
    path('wp/', include(wp_url)),
    path('admin/', admin.site.urls),
    path('clientes/', include(clientes_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
