from django.db import models
from store.models import Product


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


    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"Order {self.id}"
    
    def get_total_cost(self):
        return sum( item.get_total_const() for item in self.items.all()) 
    

class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items' ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders_items' ,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"order {self.id}"
        
    def get_total_const(self):
        return self.price * self.quantity
