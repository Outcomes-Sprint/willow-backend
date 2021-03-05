from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, object):

        return request.user == object.user

    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user