from rest_framework.permissions import BasePermission
from datetime import datetime
from datetime import timedelta
class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False

class IsValid(BasePermission):

    def has_object_permission(self, request, view, obj):
        if datetime.now().date()+timedelta(days=3) <= obj.date:
            return True
        else:
            return False
