from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone = models.IntegerField(_('Phone number'), blank=True, null=True)
    email = models.EmailField(_('Email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
