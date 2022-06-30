from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('store_auth.urls')),
    path('store/', include('store_products.urls',  namespace='store')),
    path('cart/', include('shopping_cart.urls', namespace='cart')),
    path('rating/', include('rating_section.urls', namespace='rating')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
