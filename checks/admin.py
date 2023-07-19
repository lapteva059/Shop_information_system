from django.contrib import admin
from .models import *


class CheckAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Check._meta.fields]

    class Meta:
        model = Check


admin.site.register(Check, CheckAdmin)


