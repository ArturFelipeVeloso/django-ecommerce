from django.urls import path, include
from .views import index, contact, product, products

urlpatterns = [
    path('', index, name='tela-inicial'),
    path('contato/', contact, name='tela-contato'),
    path('produto/', product, name='tela-produto'),
    path('produtos/', products, name='tela-produtos'),
]
