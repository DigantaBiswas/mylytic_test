from django import forms
from django.core.exceptions import ValidationError

from core_management.models import Order


class OrderForm(forms.ModelForm):
    def clean(self):
        products = self.cleaned_data['product']
        # if self.instance.quantity > self.instance.product.stock_in_units:
        #     raise ValidationError("Not enough stock")

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_phone', 'customer_email']
