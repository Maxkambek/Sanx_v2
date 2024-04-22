from django.urls import path
from . import views

urlpatterns = [
    path('order-create/', views.OrderCreateAPIView.as_view()),
    path('order/<int:pk>/', views.OrderDetailAPIView.as_view()),
    path('order/', views.OrderListAPIView.as_view()),
    path('order-files-create/', views.OrderFilesCreateAPIView.as_view()),
    path('order-files/<int:pk>/', views.OrderFilesUpdateAPIView.as_view()),
    path('order-applicant-create/', views.OrderApplicantCreateAPIView.as_view()),
    path('order-applicant/', views.OrderApplicantListAPIView.as_view()),
    path('order-applicant/<int:pk>/', views.OrderApplicantUpdateAPIView.as_view()),
    path('order-applicant/<int:pk>/', views.OrderApplicantRetrieveAPIView.as_view()),
]
