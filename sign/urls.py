from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign/login.html'),
    path('logout/', LogoutView.as_view(), name='sign/logout.html'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup')
]