from django.urls import path
from .views import *

urlpatterns = [
    path('get/alarms/',AlarmList.as_view({"get":"list"}),name="get_alarms")
]