from rest_framework import permissions
from fusus_test.authentication.models import UserGroups


GROUP_VERB_ACCESS_MAPPING = {
    'PUT': {UserGroups.ADMIN.value},
    'PATCH': {UserGroups.ADMIN.value},
    'GET': {UserGroups.ADMIN.value, UserGroups.VIEWER.value},
}


class OrganizationGroupPermission(permissions.BasePermission):

    def _get_user_group_set(self, request):
        return {group[0] for group in request.user.groups.all().values_list('name')}

    def _evaluate_access(self, request):
        user_group_set = self._get_user_group_set(request)
        # get allowed groups for the view
        # view can be none sometimes
        allowed_group_set = GROUP_VERB_ACCESS_MAPPING.get(
            request.method,
            set()
        )
        # check if the user belongs to at least one of
        # the allowed group(s) for the requested view
        return len(user_group_set.intersection(allowed_group_set)) > 0

    def has_permission(self, request, view):
        return self._evaluate_access(request)

    def has_object_permission(self, request, view, obj):
        return self._evaluate_access(request)
