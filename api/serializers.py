from main.models import Alarm
from rest_framework import serializers
import json

class ModeSerializerField(serializers.Field):
    
    def to_representation(self, value):
        return eval(value)

    def to_internal_value(self, data):
        return str(data)

class AlarmsSerializer(serializers.ModelSerializer):

    mode = ModeSerializerField()

    class Meta:
        model = Alarm
        fields = "__all__"
