from datetime import datetime

from django.db import models

from base.models import BaseAbstractModel


class Order(BaseAbstractModel):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.IntegerField()
    customer_email = models.CharField(max_length=255)

    class Meta:
        app_label = 'core_management'

    def __str__(self):
        return self.customer_name
