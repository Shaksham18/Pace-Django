from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db import models


class Coin(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    _1h = models.CharField(max_length=10)
    _24h = models.CharField(max_length=10)
    _7d = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=10)
    volume24h = models.CharField(max_length=100)
    supply = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    img = models.CharField(max_length=1000)

    def __str__(self):
        return self.name