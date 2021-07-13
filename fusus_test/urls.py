"""fusus_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Admin Site Config
app_name = settings.APP_NAME
admin_title = f'{app_name} Admin'

admin.sites.AdminSite.site_title = admin_title
admin.sites.AdminSite.site_header = admin_title
admin.sites.AdminSite.index_title = f'{app_name}'


apipatterns = [
    path('info/', include('fusus_test.info.urls')),
    path('users/', include('fusus_test.users.urls')),
    path('auth/', include('fusus_test.authentication.urls')),
    path('organizations/', include('fusus_test.organizations.urls')),
]

urlpatterns = [
    path(
        'api/',
        include(
            (apipatterns, 'api'),
            namespace='v1'
        ),
    ),
    path('api/basic-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
