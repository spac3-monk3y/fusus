from django.db import migrations
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    app_settings = settings.APP_SETTINGS
    if app_settings.ADMIN_EMAIL and app_settings.ADMIN_PASSWORD:
        superuser = get_user_model()(
            is_staff=True,
            is_active=True,
            is_superuser=True,
            username=app_settings.ADMIN_USERNAME,
            email=app_settings.ADMIN_EMAIL,
            last_login=timezone.now()
        )
        superuser.set_password(app_settings.ADMIN_PASSWORD.get_secret_value())
        superuser.save()
    else:
        import logging
        logger = logging.getLogger(__name__)
        logger.warning('No superuser will be created')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop)
    ]
