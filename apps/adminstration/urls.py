from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'accounts', views.AccountViewSet)
router.register(r'verify-code', views.VerifyCodeViewSet)
router.register(r'regions', views.RegionViewSet)
router.register(r'catalogs', views.CatalogViewSet)
router.register(r'user-files', views.UserFilesViewSet)
router.register(r'story', views.StoryViewSet)
router.register(r'payment-types', views.PaymentTypeViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'car-weight-types', views.CarWeightViewSet)
router.register(r'car-types', views.CarTypeViewSet)
router.register(r'car-brands', views.CarBrandViewSet)
router.register(r'car-marks', views.CarMarkViewSet)
router.register(r'colors', views.ColorViewSet)
router.register(r'transport-information', views.TransportInformationViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'transport-documents', views.TransportDocumentViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'payment', views.PaymentViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'order-applicants', views.OrderApplicantViewSet)
router.register(r'order-statuses', views.OrderStatusViewSet)
router.register(r'order-views', views.OrderViewViewSet)
router.register(r'chat', views.ChatViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('admin-login/', views.AdminLoginView.as_view()),
    path('', include(router.urls)),
]
