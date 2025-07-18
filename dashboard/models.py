from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    buying_price = models.PositiveIntegerField(null=True)
    selling_price = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}-{self.quantity} available'

    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    cost = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
    
    def save(self, *args, **kwargs):
        
        if self.product and self.order_quantity:
            self.cost = self.product.selling_price * self.order_quantity

            self.product.quantity -= self.order_quantity
            self.product.save()
        else:
            self.cost = 0
        super().save(*args, **kwargs)