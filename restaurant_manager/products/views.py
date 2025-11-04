from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Adicionar Produto'})

def product_update(request, pk):
    produto = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=produto)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Editar Produto'})

def product_delete(request, pk):
    produto = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'produto': produto})
