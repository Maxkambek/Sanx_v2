from django.urls import path, include

urlpatterns = [
    path('v1/my_auth/', include('apps.my_auth.v1.urls')),
    path('v1/main/', include('apps.main.v1.urls')),
    path('v1/order/', include('apps.order.v1.urls')),
    path('v1/admin/', include('apps.adminstration.urls'))
]
