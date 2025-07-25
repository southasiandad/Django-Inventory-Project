from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'buying_price', 'selling_price']

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'order_quantity']