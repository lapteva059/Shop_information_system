from django.db import models
from Payments.models import *


class Check(models.Model):
    # name = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_payment = models.ForeignKey(Payment, blank=True, null=True, default=None, on_delete=models.CASCADE)
    data_registration = models.DateField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name_payment

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чекы'