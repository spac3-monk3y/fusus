from . import managers
from django.db import models
from ..common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from fusus_test.organizations.models import Organization
from phonenumber_field.modelfields import PhoneNumberField


class User(BaseModel, AbstractUser):
    phone = PhoneNumberField(_('phone'), blank=True)
    email = models.EmailField(_('email'), unique=True)
    birthdate = models.DateField(_('birthdate'), blank=True, null=True)
    organization = models.ForeignKey(
        Organization,
        null=True,
        blank=True,
        related_name='users',
        on_delete=models.PROTECT
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        null=True,
        blank=True,
    )
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = managers.UserObjectsManager()

    def __str__(self) -> str:
        return f'{self.email}'
