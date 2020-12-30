from django.contrib.auth.models import UserManager
from django.db import models


class CustomUserManager(UserManager, models.Manager):
    def get_by_natural_key(self, username):
        return self.get(email=username.lower())
