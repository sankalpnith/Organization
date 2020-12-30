from core.permissions import BasePermission
from.models import RolePermission


class CanAddEmployee(BasePermission):
    permission_name = RolePermission.EMPLOYEE_CREATE


class CanEditEmployee(BasePermission):
    permission_name = RolePermission.EMPLOYEE_EDIT


class CanViewEmployee(BasePermission):
    permission_name = RolePermission.EMPLOYEE_READ


class CanDeleteEmployee(BasePermission):
    permission_name = RolePermission.EMPLOYEE_DELETE
