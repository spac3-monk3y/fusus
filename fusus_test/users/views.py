from .import permissions
from . import serializers
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from fusus_test.common.views import PerActionSerializerViewSetMixin


UserModel = get_user_model()


class UserViewSet(PerActionSerializerViewSetMixin, ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, permissions.UserGroupPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'email']
    filterset_fields = ['first_name', 'email', 'phone']
    serializer_class_mapping = {
        'create': serializers.UserCreateSerializer,
        'update': serializers.UserUpdateSerializer,
        'partial_update': serializers.UserUpdateSerializer,
    }

    def _get_user_org(self):
        return self.request.user.organization

    def get_queryset(self):
        return UserModel.objects.filter(
            organization__isnull=False,
            organization=self._get_user_org()
        )

    def perform_create(self, serializer):
        serializer.validated_data['organization_id'] = self._get_user_org().id
        return super().perform_create(serializer)
