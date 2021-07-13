from . import models
from . import serializers
from . import permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from fusus_test.common.pagination import CustomPagination
from fusus_test.users import serializers as user_serializers
from rest_framework.decorators import api_view, permission_classes

UserModel = get_user_model()


class OrganizationView(RetrieveUpdateAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.OrganizationGroupPermission
    ]


@api_view(['GET'])
@permission_classes([
    IsAuthenticated,
    permissions.OrganizationGroupPermission
])
def org_user(request, org_id, user_id):
    user = UserModel.objects.get(id=user_id)
    # validate user does in fact belong to the org
    if user.organization_id != org_id:
        return NotFound()
    serializer = user_serializers.UserShortSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([
    IsAuthenticated,
    permissions.OrganizationGroupPermission
])
def org_users(request, org_id):
    org = models.Organization.objects.get(id=org_id)
    users = org.users.all()
    paginator = CustomPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = user_serializers.UserShortSerializer(
        paginated_users,
        context={'request': request},
        many=True
    )
    return paginator.get_paginated_response(serializer.data)
