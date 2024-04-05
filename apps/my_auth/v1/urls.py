from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('verify-login/', views.LoginVerifyAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
    path('verify-register/', views.RegisterVerifyView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('delete-user/', views.DeleteAccountView.as_view())
]
