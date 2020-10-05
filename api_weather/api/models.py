from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
from datetime import timedelta
from statistics import mean


class WeatherManager(models.Manager):

    def get_average(self, begin, end, step):
        queryset = Weather.objects.filter(datetime__range=[begin, end])
        period_begin = begin
        period_end = begin + timedelta(hours=step)
        weather = []
        while period_end <= end:
            period_temperature = queryset.filter(datetime__range=[period_begin, period_end]).values_list('temperature', flat=True)
            if period_temperature:
                weather.append({
                    'datetime': period_end,
                    'temperature': mean(period_temperature)
                })
            period_begin = period_end
            period_end = period_begin + timedelta(hours=step)
        return weather

    def get_temparature(self, begin, end):
        return Weather.objects.filter(datetime__range=[begin, end])


class Weather(models.Model):
    datetime = models.DateTimeField(default=now)
    temperature = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(40)])

    objects = WeatherManager()

    class Meta:
        ordering = ['datetime']
