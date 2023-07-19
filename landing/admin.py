from django.contrib import admin
from .models import *


class AuthorizationAdmin (admin.ModelAdmin):
    list_display = ["email", "password"]


admin.site.register(Authorization, AuthorizationAdmin)


