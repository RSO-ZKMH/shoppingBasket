from django.db import models
from django.contrib.postgres.fields import ArrayField

class ShoppingBasket(models.Model):
    id = models.UUIDField()
    userId = models.UUIDField()
    productIds = models.ArrayField(models.UUIDField())