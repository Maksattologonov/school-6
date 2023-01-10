from django.contrib.auth.models import (
    BaseUserManager, PermissionsMixin, AbstractUser)
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import MyUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    ROLES = [('T', 'Teacher'), ('A', 'Admin'), ('S', 'Student')]
    username = models.CharField(max_length=255, unique=True, verbose_name=_('Имя пользователя'))
    patronymic = models.CharField(max_length=100, name='Отчество')
    surname = models.CharField(max_length=100, name='Фамилия')
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(choices=ROLES, verbose_name=_('Роли'), max_length=10)
    expiry_date = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name=_('Администратор'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Сотрудник'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.username

