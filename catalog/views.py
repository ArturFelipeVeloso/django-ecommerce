from django.shortcuts import render
from .models import Product, Category

def product_list(request):
	data = {
		'product_list': Product.objects.all()
	}
	return render(request, 'catalog/products.html', data)

def category(request, slug):
	category = Category.objects.get(slug=slug)

	data = {
		'current_category': category,
		'product_list': Product.objects.filter(category=category)
	}

	return render(request, 'catalog/products.html', data)

def product_detail(request, slug):
	prod = Product.objects.get(slug=slug)

	data = {
		'product': prod
	}

	return render(request, 'catalog/product.html', data)