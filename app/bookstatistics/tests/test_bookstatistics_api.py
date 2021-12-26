from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from core.models import BTCTRYStatistics
from bookstatistics.serializers import BTCTRYStatisticsSerializer, BTCTRYStatisticsAggrSerializer
from datetime import datetime, timedelta

BTCTRYSTATISTICS_URL = reverse("bookstatistics:btctry-daily-statistics")

class BTCTRYStatisticsApiTests(TestCase):

    def test_retrieve_BTCTRYStatistics(self):
        """Test retrieving BTCTRYStatistics"""

        BTCTRYStatistics.objects.create(
            date=datetime.now().date(),
            min_price=11.15,
            max_price=11.15,
            avg_price=11.15,
            total_volume=111.15,
        )

        BTCTRYStatistics.objects.create(
            date=datetime.now().date()-timedelta(days=1),
            min_price=12.15,
            max_price=12.15,
            avg_price=12.15,
            total_volume=122.15,
        )

        res = self.client.get(BTCTRYSTATISTICS_URL)
        print(res.data)
        btctrystatistics = BTCTRYStatistics.objects.filter(date=datetime.now().date())
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)