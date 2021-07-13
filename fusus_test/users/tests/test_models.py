import uuid
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserTestCase(TestCase):

    def test_user_creation_success_without_username_and_uuid_as_primary_key(self):
        user = UserModel(email='u1@example.com')
        user.save()
        self.assertIsNone(user.username)
        self.assertEqual(user.id, uuid.UUID(str(user.id)))

    def test_user_email_unique(self):
        email = 'u1@example.com'
        UserModel.objects.create(email=email)
        with self.assertRaises(IntegrityError):
            UserModel.objects.create(email=email)
