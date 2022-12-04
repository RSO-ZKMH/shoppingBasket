from django.db import models

class ShoppingBasket(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    store = models.CharField(max_length=255)


class User(models.Model):
    pass
