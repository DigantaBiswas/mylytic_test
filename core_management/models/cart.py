from django.db import models

from base.models import BaseAbstractModel
from core_management.models import Product, Order


class Cart(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        app_label = 'core_management'
