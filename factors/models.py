from django.db import models


class Factor(models.Model):
    factor_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    factor_country = models.CharField(max_length=64, blank=True, null=True, default=None)
    factor_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    factor_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    factor_email = models.EmailField(blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.factor_name

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

