from django.urls import path

from .views import (
    get_temperature,
    get_average
)

urlpatterns = [
    path('temperature/', get_temperature),
    path('average/', get_average),
]
