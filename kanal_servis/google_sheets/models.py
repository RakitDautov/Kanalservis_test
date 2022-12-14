from django.db import models


class Order(models.Model):

    number = models.IntegerField(unique=True)
    price_dollars = models.FloatField()
    price_rubles = models.FloatField()
    delivery_time = models.DateField()
