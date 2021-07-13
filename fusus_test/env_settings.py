import typing
import pydantic
from dotenv import load_dotenv
from pydantic import BaseSettings as PBaseSettings

load_dotenv()

OptionalStr = typing.Optional[str]


class BaseSettings(PBaseSettings):

    class Config:
        env_file = '.env'
        use_enum_values = True
        env_file_encoding = 'utf-8'


class DBSetting(BaseSettings):
    NAME: str
    USER: str
    PORT: str
    HOST: str
    ENGINE: str
    PASSWORD: pydantic.SecretStr


class DefaultDBSetting(DBSetting):
    ENGINE: str = 'django.db.backends.postgresql_psycopg2'

    class Config(DBSetting.Config):
        env_prefix = 'DB_DEFAULT_'


class AppSetting(BaseSettings):
    DEBUG: bool = True
    APP_NAME: str = 'FUSUS'
    SITE_HOST: typing.Optional[pydantic.HttpUrl]
    ADMIN_EMAIL: OptionalStr
    ADMIN_USERNAME: OptionalStr
    ADMIN_PASSWORD: pydantic.SecretStr
    DJANGO_SECRET_KEY: pydantic.SecretStr = 'django-insecure-lgn*+zx(x=1tsn5w7!wo1zd!%k6wrxpzfdm^2tfjgl+^$-jrrg'
