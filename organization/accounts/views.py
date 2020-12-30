import uuid
import accounts.serializers as serializers
from core.views import BaseModelViewSet

from .models import Employee, Role
from . import permissions as user_permissions


class LogoutViewSet(BaseModelViewSet):
    model = Employee

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.jwt_secret = str(uuid.uuid4())
        instance.save()


class EmployeeViewSet(BaseModelViewSet):

    model = Employee
    serializer_class = serializers.EmployeeSerializer

    def get_permissions(self):
        if self.action:
            if self.action.lower() == 'list':
                self.permission_classes += (
                    user_permissions.CanViewEmployee,
                )
            elif self.action.lower() == 'create':
                self.permission_classes += (
                    user_permissions.CanAddEmployee,
                )
            elif self.action.lower() == 'partial_update':
                self.permission_classes += (
                    user_permissions.CanEditEmployee,
                )
            elif self.action.lower() == 'destroy':
                self.permission_classes += (
                    user_permissions.CanDeleteEmployee,
                )
        return super().get_permissions()

    def perform_destroy(self, instance):
        instance.roles.all().delete()
        return super().perform_destroy(instance)


class RoleViewSet(BaseModelViewSet):
    model = Role
    serializer_class = serializers.RoleSerializer
