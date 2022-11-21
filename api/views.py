from django.shortcuts import get_object_or_404
from django.http import Http404
from main.models import *
from rest_framework.views import APIView
from .serializers import EncryptedAlarmsSerializer, AlarmsSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AlarmList(APIView):
    serializer_class = AlarmsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = self.get_queryset(request)
        content = AlarmList.serializer_class(content,many=True).data
        return Response(content)

    def get_queryset(self, request):
        mach = get_object_or_404(Machine, owner=request.user)
        queryset = Alarm.objects.filter(mach=mach)
        return queryset
            

