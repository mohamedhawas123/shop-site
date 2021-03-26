from django import forms
from .models import Order
# from localflavor import USZipCodeField

class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postel_code', 'city']