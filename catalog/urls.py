from django.urls import path, include
from .views import product_list, category, product_detail

urlpatterns = [
    path('catalogo/todos/', product_list, name='tela-produtos'),
    path('catalogo/<slug:slug>/', category, name='tela-produtos-categoria'),
    path('catalogo/produto/<slug:slug>/', product_detail, name='tela-produto'),
]