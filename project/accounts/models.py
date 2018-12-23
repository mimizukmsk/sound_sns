from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseuser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """ ユーザーマネージャ """

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """ メールアドレス必須 """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        if not username:
            raise ValueError('The given username must be set')
        username = self.normalize_username(username)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

