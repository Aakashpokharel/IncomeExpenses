from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path('login',RegistrationView.as_view(),name='login'),
]
