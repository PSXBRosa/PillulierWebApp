from main.models import Alarm
from rest_framework import serializers

class AlarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = ["name", "cr_t", "time", "mode", "mach", "meds"]