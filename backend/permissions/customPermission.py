from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method == "GET":
            return True
        if request.user and request.user.is_authenticated:
            return True
        return False
