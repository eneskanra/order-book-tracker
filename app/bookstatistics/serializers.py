from rest_framework import serializers
from core.models import BTCTRYStatistics
from django.db.models import Sum, F, Q, Count, Min, Max, Avg
from datetime import datetime, timedelta

class BTCTRYStatisticsSerializer(serializers.ModelSerializer):
    """Serializer for BTCTRYStatistics objects"""

    class Meta:
        model = BTCTRYStatistics
        exclude = ('id',)


class BTCTRYStatisticsAggrSerializer(serializers.Serializer):
    """Serializer for BTCTRYStatistics Aggregated objects"""
    date = serializers.SerializerMethodField()
    min_min_price = serializers.SerializerMethodField()
    max_min_price = serializers.SerializerMethodField()
    avg_min_price = serializers.SerializerMethodField()
    min_max_price = serializers.SerializerMethodField()
    max_max_price = serializers.SerializerMethodField()
    avg_max_price = serializers.SerializerMethodField()
    min_avg_price = serializers.SerializerMethodField()
    max_avg_price = serializers.SerializerMethodField()
    avg_avg_price = serializers.SerializerMethodField()
    min_total_volume = serializers.SerializerMethodField()
    max_total_volume = serializers.SerializerMethodField()
    avg_total_volume = serializers.SerializerMethodField()

    class Meta:
        model = BTCTRYStatistics
        fields = '__all__'
    
    def get_date(self, obj):
        date = (self.context['today'])
        return date

    def get_min_min_price(self, obj):
        min_min_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(min_min_price=Min('min_price'))['min_min_price'])
        return min_min_price
    
    def get_max_min_price(self, obj):
        max_min_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(max_min_price=Max('min_price'))['max_min_price'])
        return max_min_price
    
    def get_avg_min_price(self, obj):
        avg_min_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(avg_min_price=Avg('min_price'))['avg_min_price'])
        return avg_min_price

    def get_min_max_price(self, obj):
        min_max_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(min_max_price=Min('max_price'))['min_max_price'])
        return min_max_price
    
    def get_max_max_price(self, obj):
        max_max_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(max_max_price=Max('max_price'))['max_max_price'])
        return max_max_price
    
    def get_avg_max_price(self, obj):
        avg_max_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(avg_max_price=Avg('max_price'))['avg_max_price'])
        return avg_max_price
    
    def get_min_avg_price(self, obj):
        min_avg_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(min_avg_price=Min('avg_price'))['min_avg_price'])
        return min_avg_price
    
    def get_max_avg_price(self, obj):
        max_avg_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(max_avg_price=Max('avg_price'))['max_avg_price'])
        return max_avg_price
    
    def get_avg_avg_price(self, obj):
        avg_avg_price = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                        .aggregate(avg_avg_price=Avg('avg_price'))['avg_avg_price'])
        return avg_avg_price
    
    def get_min_total_volume(self, obj):
        min_total_volume = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                            .aggregate(min_total_volume=Min('total_volume'))['min_total_volume'])
        return min_total_volume
    
    def get_max_total_volume(self, obj):
        max_total_volume = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                            .aggregate(max_total_volume=Max('total_volume'))['max_total_volume'])
        return max_total_volume
    
    def get_avg_total_volume(self, obj):
        avg_total_volume = (BTCTRYStatistics.objects.filter(date__gte=self.context['today']-timedelta(days=self.context['day']))
                            .aggregate(avg_total_volume=Avg('total_volume'))['avg_total_volume'])
        return avg_total_volume


