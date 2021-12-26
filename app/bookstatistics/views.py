from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from core.models import BTCTRYStatistics
from bookstatistics import serializers
from itertools import chain
from django.db.models import Sum, F, Q, Count, Min, Max, Avg
from datetime import datetime


class BTCTRYStatisticsDailyAPIView(ListAPIView):
    """View for BTCTRYStatistics daily info"""
    queryset = BTCTRYStatistics.objects.filter(date=datetime.now().date())
    serializer_class = serializers.BTCTRYStatisticsSerializer


class BTCTRYStatisticsWeeklyAPIView(ListAPIView):
    """View for BTCTRYStatistics weekly info"""
    def get_queryset(self):
        queryset = {'date': datetime.now().date()}
        return queryset
    
    def get_serializer_context(self):
        today = datetime.now().date()
        context = super().get_serializer_context()
        context["day"] = 6
        context["today"] = today
        return context

    serializer_class = serializers.BTCTRYStatisticsAggrSerializer


class BTCTRYStatisticsMonthlyAPIView(ListAPIView):
    """View for BTCTRYStatistics monthly info"""

    def get_queryset(self):
        queryset = BTCTRYStatistics.objects.aggregate(Min('min_price'))
        return queryset
    
    def get_serializer_context(self):
        today = datetime.now().date()
        context = super().get_serializer_context()
        context["day"] = 29
        context["today"] = today
        return context

    serializer_class = serializers.BTCTRYStatisticsAggrSerializer