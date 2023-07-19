from django.db import models
from factors.models import *
from clients.models import *


class Transport(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    factor_name = models.ForeignKey(Factor, blank=True, null=True, default=None, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, blank=True, null=True, default=None, on_delete=models.CASCADE)
    type_car = models.CharField(max_length=64, blank=True, null=True, default=None)
    carry = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_delivery = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.price_delivery, self.name)

    class Meta:
        verbose_name = 'Транстпорт'
        verbose_name_plural = 'Транспорты'

