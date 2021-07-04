from datetime import datetime

from django.db import models

from base.models import BaseAbstractModel


class Order(BaseAbstractModel):
    # order_number = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.IntegerField()
    customer_email = models.CharField(max_length=255)
    # product = models.ManyToManyField(Product)
    # quantity = models.IntegerField()
    # cart = models.ManyToManyField(Cart)

    class Meta:
        app_label = 'core_management'

    def __str__(self):
        return self.customer_name
