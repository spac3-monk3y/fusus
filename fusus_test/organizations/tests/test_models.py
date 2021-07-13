from ..models import Organization
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class OrganizationCase(TestCase):
    # TODO
    ...
