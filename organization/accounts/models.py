import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from core.models import BaseModel
from.managers import CustomUserManager


def string_uuid():
    return str(uuid.uuid4())


class Employee(BaseModel, AbstractBaseUser):
    emp_id = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    position = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    jwt_secret = models.CharField(default=string_uuid, max_length=36)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def permissions(self):
        user_permissions = {}
        for user_role_relations in self.roles.all():
            user_permissions.update(user_role_relations.perm_dict())
        return user_permissions


class Role(BaseModel):
    name = models.CharField(unique=True, max_length=50)


class UserRoleRelationship(BaseModel):
    user = models.ForeignKey(Employee, related_name='roles', on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, related_name='role_users', on_delete=models.DO_NOTHING)

    def perm_dict(self):
        role_perms = {
            perm_slug: True for perm_slug in self.role.permissions.values_list(
                'slug', flat=True
            )
        }
        return role_perms


class RolePermission(BaseModel):
    EMPLOYEE_CREATE = 'employee_create'
    EMPLOYEE_READ = 'employee_read'
    EMPLOYEE_EDIT = 'employee_edit'
    EMPLOYEE_DELETE = 'employee_delete'
    ROOM_CREATE = 'conf_room_create'
    ROOM_READ = 'conf_room_read'
    ROOM_EDIT = 'conf_room_edit'
    ROOM_DELETE = 'conf_room_delete'

    PERMISSION_CHOICES = (
        (EMPLOYEE_CREATE, 'Employee Create',),
        (EMPLOYEE_READ, 'Employee Read',),
        (EMPLOYEE_EDIT, 'Employee Edit',),
        (EMPLOYEE_DELETE, 'Employee Delete',),
        (ROOM_CREATE, 'Room Create',),
        (ROOM_READ, 'Room Read',),
        (ROOM_EDIT, 'Room Edit',),
        (ROOM_DELETE, 'Room Delete',),
    )

    role = models.ForeignKey(Role, related_name='permissions', on_delete=models.DO_NOTHING)
    slug = models.CharField(
        max_length=100,
        choices=PERMISSION_CHOICES,
    )

