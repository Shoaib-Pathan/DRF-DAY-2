from django.urls import path
from .views import first_api, SecondAPI, ThirdApi, fetchperticular

urlpatterns = [
    path('first/', first_api),
    path('second/', SecondAPI.as_view()),
    path('third/', ThirdApi.as_view()),
    path('third/<int:pk>', fetchperticular.as_view())
]