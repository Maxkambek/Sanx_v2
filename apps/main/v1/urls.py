from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subscriptions', views.SubscriptionViewSet)
# router.register(r'notifications', views.NotificationViewSet)
router.register(r'story', views.StoryViewSet)

urlpatterns = [
    path('regions/', views.RegionList.as_view(), name='regions'),
    path('catalogs/', views.CatalogList.as_view(), name='catalogs'),
    path('user-files/', views.UserFilesList.as_view(), name='user-files'),
    path('user-files-create/', views.UserFilesCreate.as_view(), name='user-files-create'),
    path('user-files-rud/', views.UserFilesRUD.as_view(), name='user-files-rud'),
    path('payment-type/', views.PaymentTypeList.as_view(), name='payment-type'),
    path('currency/', views.CurrencyList.as_view(), name='currency'),
    path('car-weight-type/', views.CarWeightTypeList.as_view(), name='car-weigth-type'),
    path('car-type/', views.CarTypeList.as_view(), name='car-type'),
    path('car-brand/', views.CarBrandList.as_view(), name='car-brand'),
    path('car-mark/', views.CarMarkList.as_view(), name='car-mark'),
    path('color/', views.ColorList.as_view(), name='color'),
    path('notifications/', views.NotificationListAPIView.as_view(), name='color'),
    path('notification/<int:pk>/', views.NotificationUpdate.as_view(), name='color'),
    path('transport-information/', views.TransportInformationList.as_view(), name='transport-information'),
    path('transport-information-create/', views.TransportInformationCreate.as_view(),
         name='transport-information-create'),
    path('', include(router.urls)),
    path('user-rating-create/', views.UserRatingCreate.as_view(), name='user-rating-create'),
]
