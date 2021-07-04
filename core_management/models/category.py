from django.urls import reverse

from base.models import BaseAbstractModel
from django.db import models


class Category(BaseAbstractModel):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'core_management'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-list')
