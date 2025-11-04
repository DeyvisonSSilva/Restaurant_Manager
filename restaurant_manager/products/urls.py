from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('novo/', views.product_create, name='product_create'),
    path('<int:pk>/editar/', views.product_update, name='product_update'),
    path('<int:pk>/excluir/', views.product_delete, name='product_delete'),
]
