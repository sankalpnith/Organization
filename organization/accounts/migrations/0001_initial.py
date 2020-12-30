# Generated by Django 3.1.4 on 2020-12-29 20:05

import accounts.managers
import accounts.models
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=core.models.string_uuid, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('emp_id', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=20)),
                ('team', models.CharField(max_length=20)),
                ('jwt_secret', models.CharField(default=accounts.models.string_uuid, max_length=36)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(default=core.models.string_uuid, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRoleRelationship',
            fields=[
                ('id', models.CharField(default=core.models.string_uuid, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='role_users', to='accounts.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='roles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.CharField(default=core.models.string_uuid, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(choices=[('employee_create', 'Employee Create'), ('employee_read', 'Employee Read'), ('employee_edit', 'Employee Edit'), ('employee_delete', 'Employee Delete'), ('conf_room_create', 'Room Create'), ('conf_room_read', 'Room Read'), ('conf_room_edit', 'Room Edit'), ('conf_room_delete', 'Room Delete')], max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='permissions', to='accounts.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]