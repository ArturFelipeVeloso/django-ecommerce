from django.urls import path, include
from .views import index, contact

from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

urlpatterns = [
    path('', index, name='tela-inicial'),
    path('contato/', contact, name='tela-contato'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]