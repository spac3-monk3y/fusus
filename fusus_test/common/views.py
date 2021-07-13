from django.db.models import Model
from rest_framework.serializers import Serializer


class PerActionSerializerViewSetMixin:
    serializer_class_mapping: dict

    def get_serializer_class(self) -> Serializer:
        return self.serializer_class_mapping.get(
            self.action,
            self.serializer_class
        )


class AddUserBeforeModelSerializerSaveMixin:
    user_field_name: str = 'created_by'

    def perform_create(self, serializer: Serializer) -> None:
        serializer.validated_data[self.user_field_name] = self.request.user
        super(
            AddUserBeforeModelSerializerSaveMixin,
            self
        ).perform_create(serializer)


class FilterListByAuthUserViewMixin:
    model: Model
    user_field: str

    # TODO: update to accept a manifest using request params to filter response

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(
            **{
                self.user_field: user
            }
        )


class FilterListByCreatorViewMixin(FilterListByAuthUserViewMixin):
    user_field: str = 'created_by'
