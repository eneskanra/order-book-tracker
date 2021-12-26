from django.db import models
from django.utils.timezone import now
from django.db.models import Sum, F, Q, Count, Max, Avg
# Create your models here.


class BTCTRY(models.Model):
    """BTCTRY Order Book record"""
    min_price = models.FloatField()
    max_price = models.FloatField()
    avg_price = models.FloatField()
    total_volume = models.FloatField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.timestamp)


class BTCTRYStatistics(models.Model):
    """BTCTRY Order Book Daily-24h record"""
    date = models.DateField(unique=True)
    min_price = models.FloatField()
    max_price = models.FloatField()
    avg_price = models.FloatField()
    total_volume = models.FloatField()

    def __str__(self):
        return str(self.date)

    
