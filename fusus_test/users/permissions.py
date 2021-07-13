from rest_framework import permissions
from fusus_test.authentication.models import UserGroups

allowed_update_groups = {UserGroups.ADMIN.value, UserGroups.USER.value}

GROUP_ACTION_ACCESS_MAPPING = {
    'create': {UserGroups.ADMIN.value},
    'destroy': {UserGroups.ADMIN.value},
    'update': allowed_update_groups,
    'partial_update': allowed_update_groups,
    'list': {UserGroups.ADMIN.value, UserGroups.VIEWER.value},
    'retrieve': {UserGroups.ADMIN.value, UserGroups.VIEWER.value, UserGroups.USER.value},
}


class UserGroupPermission(permissions.BasePermission):

    # TODO: add cache
    def _get_user_group_set(self, request):
        return {group[0] for group in request.user.groups.all().values_list('name')}

    def _evaluate_access(self, view_action, user_group_set):
        # get allowed groups for the view
        # view can be none sometimes
        allowed_group_set = GROUP_ACTION_ACCESS_MAPPING.get(
            view_action,
            set()
        )
        # check if the user belongs to at least one of
        # the allowed group(s) for the requested view
        return len(user_group_set.intersection(allowed_group_set)) > 0

    def has_permission(self, request, view):
        # get user's groups
        user_group_set = self._get_user_group_set(request)
        return self._evaluate_access(view.action, user_group_set)

    def has_object_permission(self, request, view, obj):
        user_group_set = self._get_user_group_set(request)
        if view.action in ['update', 'partial_update'] and \
                UserGroups.USER.value in user_group_set and \
                UserGroups.ADMIN.value not in user_group_set:
            return obj == request.user

        return self._evaluate_access(view.action, user_group_set)
