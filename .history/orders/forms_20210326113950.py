from django import forms
from .models import Order
from localeflavor.us.forms import USZipCodeField

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postel_code', 'city']