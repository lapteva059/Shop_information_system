from django.db import models


class Authorization(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)




