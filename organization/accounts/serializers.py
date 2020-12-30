from rest_framework import serializers
from .models import Employee, Role, UserRoleRelationship
from django.db import transaction


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            'name',
        )


class UserRoleRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoleRelationship
        fields = (
            'id',
            'role',
            'user',
            )
        read_only_fields = (
            'id',
        )
        extra_kwargs = {
            'role': {'required': True},
            'user': {'required': True},
            }


class EmployeeSerializer(serializers.ModelSerializer):

    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=True, write_only=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'emp_id',
            'email',
            'name',
            'mobile_number',
            'position',
            'team',
            'role',
        )
        read_only_fields = (
            'id',
        )
        extra_kwargs = {
            'emp_id': {'required': True},
            'email': {'required': True},
            'name': {'required': True},
            'mobile_number': {'required': True},
            'position': {'required': True},
            'team': {'required': True},
        }

    def create(self, validated_data):
        role = validated_data.pop('role', None)
        with transaction.atomic():
            user = super().create(validated_data)

            user_role_data = {'role': role.id, 'user': user.id}
            user_role_relationships = UserRoleRelationshipSerializer(
                data=user_role_data,
                context=self.context,
            )
            user_role_relationships.is_valid(raise_exception=True)
            user_role_relationships.save()
            return user

    def update(self, instance, validated_data):
        role = validated_data.pop('role', None)
        with transaction.atomic():
            instance = super().update(instance, validated_data)
            if role.id != instance.roles.first().role.id:
                instance.roles.all().delete()
                user_role_data = {'role': role.id, 'user': instance.id}
                user_role_relationships = UserRoleRelationshipSerializer(
                    data=user_role_data,
                    context=self.context,
                )
                user_role_relationships.is_valid(raise_exception=True)
                user_role_relationships.save()
            return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['role_id'] = instance.roles.first().role.id
        response['role'] = instance.roles.first().role.name
        return response
