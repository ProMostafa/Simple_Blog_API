from rest_framework import permissions
from .models import Post

class UpdateOwnPost(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author