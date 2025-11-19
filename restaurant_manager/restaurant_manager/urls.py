from django.contrib import admin
from django.urls import path, include
from pedidos.views import fazer_pedido, pedido_sucesso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('fazer-pedido/', fazer_pedido, name='fazer_pedido'),
    path('pedido-sucesso/<int:pedido_id>/', pedido_sucesso, name='pedido_sucesso'),
]