import datetime

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):

    @classmethod
    def normalize_username(cls, username):
        username = username or ''
        try:
            username_name = username.strip()
        except ValueError:
            pass
        else:
            username = username_name
        return username

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('Users must have an username address'))
        username = self.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def _create_user(self, username,  password, **extra_fields):
        if not username:
            raise ValueError('Users must have an email address')
        username = self.normalize_username(username)

        user = self.model(
            username=username,
            is_staff=True,
            is_active=True,
            is_superuser=True,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def _create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, **extra_fields)
        return user