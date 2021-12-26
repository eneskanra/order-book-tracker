from django.urls import path, include

from bookstatistics import views


app_name = "bookstatistics"

urlpatterns = [
    path('btctry/daily/', views.BTCTRYStatisticsDailyAPIView.as_view(), name='btctry-daily-statistics'),
    path('btctry/weekly/', views.BTCTRYStatisticsWeeklyAPIView.as_view(), name='btctry-weekly-statistics'),
    path('btctry/monthly/', views.BTCTRYStatisticsMonthlyAPIView.as_view(), name='btctry-monthly-statistics')
]