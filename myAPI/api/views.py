from django.shortcuts import get_object_or_404
from django.http import Http404
from main.models import *
from rest_framework import generics
from .serializers import AlarmsSerializer
import rsa

class AlarmList(generics.ListCreateAPIView):
    serializer_class = AlarmsSerializer
    
    @staticmethod
    def _confirm_identity(public_key):
        # NOTE Since the query parameters get HTTP decoded, all the
        # "+" signs in the request MUST be encoded as "%2B"
        obj = get_object_or_404(Machine, pubk=public_key)
        return obj

    def get_queryset(self):
        pubk = self.request.query_params.get('pubk', False)
        if pubk:
            mach = self._confirm_identity(pubk)
            queryset = Alarm.objects.filter(mach=mach)
            return queryset
        else:
            raise Http404
            

