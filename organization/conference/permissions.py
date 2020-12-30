from core.permissions import BasePermission
from accounts.models import RolePermission



class CanCreateRoom(BasePermission):
    permission_name = RolePermission.ROOM_CREATE


class CanEditRoom(BasePermission):
    permission_name = RolePermission.ROOM_EDIT


class CanViewRoom(BasePermission):
    permission_name = RolePermission.ROOM_READ


class CanDeleteRoom(BasePermission):
    permission_name = RolePermission.ROOM_DELETE
