from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


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

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLES = [('T', 'Teacher'), ('A', 'Admin'), ('S', 'Student')]
    username = models.CharField(max_length=255, unique=True, verbose_name=_('Имя пользователя'))
    name = models.CharField(max_length=100, name='Имя')
    patronymic = models.CharField(max_length=100, name='Отчество')
    surname = models.CharField(max_length=100, name='Фамилия')
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(choices=ROLES, verbose_name=_('Роли'), max_length=10)
    expiry_date = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name=_('Администратор'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Сотрудник'))
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname', 'role']

    def __str__(self):
        return self.username

    def has_permisson(self, request, view):
        return bool(request.user and request.user.is_admin)

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_out_of_credits(self):
        "Is the user out  of credits?"
        return self.credits > 0

    @property
    def has_sufficient_credits(self, cost):
        return self.credits - cost >= 0
