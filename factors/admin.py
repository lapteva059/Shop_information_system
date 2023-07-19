from django.contrib import admin
from .models import *


class FactorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Factor._meta.fields]

    class Meta:
        model = Factor


admin.site.register(Factor, FactorAdmin)


