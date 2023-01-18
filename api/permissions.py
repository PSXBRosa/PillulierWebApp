from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from main.models import Machine

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        mach = request.data.get("mach", None)
        mach_object = get_object_or_404(Machine, id=mach)
        user = request.user
        return mach_object.owner == user
        
