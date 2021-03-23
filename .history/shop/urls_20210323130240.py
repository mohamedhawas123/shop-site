
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

app_name = 'store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupon/', include('coupons.urls', namespace="coupons")),
    path('rosetta/', include('rosetta.urls')),
    path('', include('store.urls', namespace="store"),),
    path('orders/', include('orders.urls', namespace='orders'), ),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)