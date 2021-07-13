import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        unique=True
    )

    class Meta:
        abstract = True


class CreatedUpdatedTsMixin(models.Model):
    """Adds created & modified timestamp to model"""
    created_at = models.DateTimeField(
        _('created_at'),
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        _('updated_at'),
        auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    """Adds description to model"""
    description = models.TextField(_('description'), null=True, blank=True)

    class Meta:
        abstract = True


class CreatedByMixin(models.Model):
    """Adds owner link to model"""
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True


class CommonFieldMixin(
    DescriptionMixin,
    CreatedUpdatedTsMixin,
):

    class Meta:
        abstract = True


class CleanBeforeSaveMixin:
    """
    Calls the clean method for model validation before save.
    """

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CleanBeforeSaveMixin, self).save(*args, **kwargs)
