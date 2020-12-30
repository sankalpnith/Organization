from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    permission_name = None

    def check_permission(self, request, view):
        facility_perms = request.user.permissions
        return facility_perms.get(self.permission_name, False)

    def has_permission(self, request, view):
        return self.check_permission(request, view)
