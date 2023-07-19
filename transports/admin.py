from django.contrib import admin
from .models import *


class TransportAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Transport._meta.fields]

    class Meta:
        model = Transport

admin.site.register(Transport, TransportAdmin)


