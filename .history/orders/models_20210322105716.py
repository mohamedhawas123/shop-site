from django.db import models
from store.models import Product
from coupons.models import Coupon
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postel_code = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    braintree_id=  models.CharField(max_length=150, blank=True)
    coupon = models.ForeignKey(Coupon, related_name='orders', blank=True, null=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,  validators=[MinValueValidator(0), MaxValueValidator(100)])



    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"Order {self.id}"
    
    def get_total_cost(self):
        total_cost = sum( item.get_total_const() for item in self.items.all())
        return total_cost - total_cost *  (self.discount / Dec)
    

class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items' ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders_items' ,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"order {self.id}"
        
    def get_total_const(self):
        return self.price * self.quantity
