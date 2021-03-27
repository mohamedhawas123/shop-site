from django.shortcuts import render, get_object_or_404
from .models  import Category, Product
from cart.forms import CartAddProduct
from .recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug= category_slug)
        products = products.filter(category=category)

    return render(request, 'store/product/list.html', {'category': category,'categories':categories, 'products':products})



def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug, id=id, available=True)
    cart_product_form = CartAddProduct()
    r = Recommender()
    recommend_products = r.suggest_products_for([product], 4)

    return render(request, 'store/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'recommend_products': recommend_products})



