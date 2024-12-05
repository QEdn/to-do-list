from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `author`.
        return obj.author == request.user
