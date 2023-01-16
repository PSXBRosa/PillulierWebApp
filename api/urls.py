from django.urls import path
from .views import AlarmList

urlpatterns = [
    path('get/alarms/',AlarmList.as_view(),name="get_alarms")
]