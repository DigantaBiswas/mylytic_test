from django.db import models
# Create your models here.
from django.urls import reverse

from base.models import BaseAbstractModel
from core_management.models.category import Category


class Product(BaseAbstractModel):
    product_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    stock_in_units = models.IntegerField(default=0)

    class Meta:
        app_label = 'core_management'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-list')

    def update_stock_after_order(self, quantity):
        self.stock_in_units = self.stock_in_units - quantity
        self.save()