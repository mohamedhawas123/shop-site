from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created
from django.urls import reverse



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        order_created.delay(order.id)
        request.session['order_id'] = order.id
        return redirect(reverse('payment:process'))
    
    else:
        form = OrderCreateForm()
        
    
    return render(request, 'orders/order/create.html', {'form': form } )
