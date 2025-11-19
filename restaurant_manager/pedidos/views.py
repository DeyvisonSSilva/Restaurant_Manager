from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from products.models import Product 
from .models import Pedido, ItemPedido

def fazer_pedido(request):
    products = Product.objects.all()

    if request.method == 'POST':
        nome_cliente = request.POST.get('nome_cliente')
        
        
        if not nome_cliente:
            messages.error(request, "O campo 'Nome do Cliente' é obrigatório para fazer o pedido.")
            return render(request, 'pedidos/fazer_pedido.html', {'produtos': products})

        
        try:
            pedido = Pedido.objects.create(nome_cliente=nome_cliente, status='aberto')
            has_items = False
            
            
            for key, value in request.POST.items():
                if key.startswith("prod_") and value and int(value) > 0:
                    prod_id = key.split("_")[1]
                    produto = Product.objects.get(id=prod_id)
                    ItemPedido.objects.create(
                        pedido=pedido,
                        produto=produto,
                        quantidade=int(value)
                    )
                    has_items = True

            
            if not has_items:
                pedido.delete()
                messages.error(request, "Selecione pelo menos um item para enviar o pedido.")
                return render(request, 'pedidos/fazer_pedido.html', {'produtos': products})

            messages.success(request, "Pedido realizado com sucesso!")
            return redirect('pedido_sucesso', pedido_id=pedido.id)

        
        except Exception as e:
            messages.error(request, f"Ocorreu um erro inesperado ao processar o pedido. Detalhes: {e}")
            return render(request, 'pedidos/fazer_pedido.html', {'produtos': products})

    
    return render(request, 'pedidos/fazer_pedido.html', {'produtos': products})

def pedido_sucesso(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/pedido_sucesso.html', {'pedido': pedido})