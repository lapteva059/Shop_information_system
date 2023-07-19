from django.db import models
from factors.models import *


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    factor_name = models.ForeignKey(Factor, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price_purchasing = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

