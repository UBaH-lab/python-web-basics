from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from catalog.models import Product
from catalog.forms import ProductForm


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)  # 6 товаров на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'page_obj': page_obj})


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})