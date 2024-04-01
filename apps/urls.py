from django.urls import path, include

urlpatterns = [
    path('v1/auth/', include('apps.auth.v1.urls')),
    path('v1/main/', include('apps.main.v1.urls')),
    path('v1/order/', include('apps.order.v1.urls'))
]
