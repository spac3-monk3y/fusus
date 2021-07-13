from django.db import models


class UserGroups(models.TextChoices):
    USER = 'User'
    VIEWER = 'Viewer'
    ADMIN = 'Administrator'
