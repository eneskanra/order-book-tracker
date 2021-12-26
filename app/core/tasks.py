from django.utils.timezone import make_aware

from celery import shared_task 
import requests
from datetime import datetime, timedelta
from core.models import BTCTRY, BTCTRYStatistics

@shared_task 
def fetch_data():
    response = requests.get('https://www.bitexen.com/api/v1/order_book/BTCTRY/')
    result = response.json()
    if result["status"] == "success":
        ticker = result["data"]["ticker"]
        date_dt = datetime.fromtimestamp(float(ticker["timestamp"]))
        date = date_dt.date()
        record = {
            "min_price": ticker["low_24h"], 
            "max_price": ticker["high_24h"], 
            "avg_price": ticker["avg_24h"], 
            "total_volume": ticker["volume_24h"], 
            "timestamp": make_aware(date_dt) 
        }  
        record_object = BTCTRY.objects.create(**record)
        record_object.save()
        statistics_record = {
            "date": date,
            "min_price": ticker["low_24h"], 
            "max_price": ticker["high_24h"], 
            "avg_price": ticker["avg_24h"], 
            "total_volume": ticker["volume_24h"]
        }
        obj, created = BTCTRYStatistics.objects.update_or_create(
            date=date,
            defaults={**statistics_record}
        )
       

