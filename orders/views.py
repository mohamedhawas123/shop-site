from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    
    else:
        form = OrderCreateForm()
        order_created(order.id)
    
    return render(request, 'orders/order/create.html', {'form': form } )
