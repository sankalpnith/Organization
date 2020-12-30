from django.core.management import BaseCommand
from accounts.models import Role, RolePermission, Employee, UserRoleRelationship


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        role_permission = [
            {
                'role': 'ADMIN',
                'permissions': [
                    'employee_create',
                    'employee_read',
                    'employee_edit',
                    'employee_delete',
                    'conf_room_create',
                    'conf_room_read',
                    'conf_room_edit',
                    'conf_room_delete',
                ]
            },
            {
                'role': 'ENGG MANAGER',
                'permissions': [
                    'employee_create',
                    'employee_read',
                    'employee_edit',
                ]
            },
            {
                'role': 'OFFICE MANAGER',
                'permissions': [
                    'conf_room_create',
                    'conf_room_read',
                    'conf_room_edit',
                ]
            },
            {
                'role': 'DEFAULT',
                'permissions': [
                    'conf_room_read',
                    'employee_read',
                ]
            }
        ]
        for role_permission_dict in role_permission:
            role_obj = Role.objects.get_or_create(
                name=role_permission_dict.get('role'),
                defaults={
                    'name': role_permission_dict.get('role'),
                },
            )
            for permission in role_permission_dict['permissions']:
                RolePermission.objects.get_or_create(
                    role=role_obj[0],
                    slug=permission,
                    defaults={
                        'role': role_obj[0],
                        'slug': permission,
                    },
                )

        user_list = [
            {
                'emp_id': 'A001',
                'email': 'admin@gmail.com',
                'name': 'Admin',
                'mobile_number': '1234567890',
                'position': 'CEO',
                'role': 'ADMIN',
                'team': 'Management',
            },
            {
                'emp_id': 'B001',
                'email': 'engg_manager@gmail.com',
                'name': 'Engineering Manager',
                'mobile_number': '4322345678',
                'position': 'CFO',
                'role': 'ENGG MANAGER',
                'team': 'Management',
            },
            {
                'emp_id': 'C001',
                'email': 'office_manager@gmail.com',
                'name': 'Office Manager',
                'mobile_number': '5678901234',
                'position': 'Director Engineering',
                'role': 'OFFICE MANAGER',
                'team': 'Management',
            },
            {
                'emp_id': 'D001',
                'email': 'default@gmail.com',
                'name': 'Default User',
                'mobile_number': '5678901236',
                'position': 'SDE',
                'role': 'DEFAULT',
                'team': 'Developer',
            }
        ]

        for user_dict in user_list:
            role_obj = Role.objects.get(name=user_dict['role'])
            u = Employee.objects.create(
                emp_id=user_dict['emp_id'],
                email=user_dict['email'],
                name=user_dict['name'],
                mobile_number=user_dict['mobile_number'],
                position=user_dict['position'],
                team=user_dict['team'],
            )
            u.set_password("Test@123")
            u.save()
            UserRoleRelationship.objects.create(
                user=u,
                role=role_obj
            )
