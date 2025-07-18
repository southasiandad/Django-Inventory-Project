from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'General Inventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'buying_price', 'selling_price')
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'order_quantity', 'cost', 'date')
    list_filter = ('staff',)

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

# admin.site.unregister(Group)