from django.db import models
from django.contrib.postgres.fields import ArrayField

class ShoppingBasket(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    userId = models.IntegerField()
    productIds = ArrayField(models.IntegerField())