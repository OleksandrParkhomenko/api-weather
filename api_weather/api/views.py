from django.http import JsonResponse
from .models import Weather
from datetime import datetime


def get_average(request):
    begin_str = request.GET.get('begin')
    end_str = request.GET.get('end')
    step = float(request.GET.get('step'))
    begin_datetime = datetime.strptime(begin_str, '%m/%d/%y')
    end_datetime = datetime.strptime(end_str, '%m/%d/%y')
    queryset = list(Weather.objects.get_average(begin_datetime, end_datetime, step))
    return JsonResponse({'data': list(queryset)})


def get_temperature(request):
    begin_str = request.GET.get('begin')
    end_str = request.GET.get('end')
    begin_datetime = datetime.strptime(begin_str, '%m/%d/%y')
    end_datetime = datetime.strptime(end_str, '%m/%d/%y')
    queryset = list(Weather.objects.get_temparature(begin_datetime, end_datetime).values())
    return JsonResponse({'data': list(queryset)})
