from django.db import models
from django.utils.timezone import now
# Create your models here.


class BTCTRY(models.Model):
    """BTCTRY Order Book record"""
    min_price = models.FloatField()
    max_price = models.FloatField()
    avg_price = models.FloatField()
    total_volume = models.FloatField()
    timestamp = models.DateTimeField(default=now)


class BTCTRYStatistics(models.Model):
    """BTCTRY Order Book records"""
    date = models.DateField(unique=True)
    min_price = models.FloatField()
    max_price = models.FloatField()
    avg_price = models.FloatField()
    total_volume = models.FloatField()
