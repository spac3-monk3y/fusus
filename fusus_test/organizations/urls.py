from . import views
from django.urls import path

urlpatterns = [
    path('<uuid:pk>/', view=views.OrganizationView.as_view(), name='organization'),
    path('<uuid:org_id>/users/', view=views.org_users, name='organization-users'),
    path(
        '<uuid:org_id>/users/<uuid:user_id>',
        view=views.org_user,
        name='organization-user'
    )
]
