from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from apps.tools.helpers import USER_TYPE, USER_STATUS


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=22, unique=True)

    first_name = models.CharField(max_length=123, null=True, blank=True)
    last_name = models.CharField(max_length=123, null=True, blank=True)
    middle_name = models.CharField(max_length=123, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user/avatars/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user_status = models.CharField(choices=USER_STATUS, max_length=20, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=20, default='Client')

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class VerifyCode(models.Model):
    phone = models.CharField(max_length=22)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
