from django.shortcuts import get_object_or_404
from django.http import Http404
from main.models import *
from .serializers import AlarmsSerializer
from .permissions import IsOwner

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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

class AlarmPost(APIView):
    serializer_class = AlarmsSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def post(self, request, format=None):
        serializer = AlarmPost.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            

