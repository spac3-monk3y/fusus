from django.db import models
from django.utils.translation import gettext_lazy as _
from ..common.models import BaseModel, CommonFieldMixin
from phonenumber_field.modelfields import PhoneNumberField


class Organization(BaseModel, CommonFieldMixin):
    name = models.CharField(_('name'), max_length=100)
    phone = PhoneNumberField(_('phone'), blank=True)
    address = models.CharField(_('address'), max_length=200, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
