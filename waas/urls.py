from atexit import register
from django.urls import path
from . import views

urlpatterns = [
    path('test-auth/',views.TestAuthAPIView.as_view(), name = 'test-auth'),
    path('register-beneficiary/',views.RegisterBeneficiaryAPIView.as_view(), name = 'register-beneficiary'),
]