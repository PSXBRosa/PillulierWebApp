from main.models import Alarm
from rest_framework import serializers
import json

class AlarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = "__all__"
        