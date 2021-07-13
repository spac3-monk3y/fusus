import typing
from django.db.models import Model
from django.shortcuts import resolve_url
from django.utils.html import format_html
from django.utils.safestring import SafeText
from django.contrib.admin.templatetags.admin_urls import admin_urlname


def model_admin_url(obj: Model, name: str = None) -> str:
    url = resolve_url(admin_urlname(obj._meta, SafeText('change')), obj.id)
    return format_html('<a href="{}">{}</a>', url, name or str(obj))


def admin_link(obj: Model, field: str, display_name: str = None) -> typing.Optional[str]:
    if (ref_obj := getattr(obj, field)):
        return model_admin_url(ref_obj, display_name)
