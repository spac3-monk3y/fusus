from rest_framework import serializers
from django.contrib.auth import get_user_model
from fusus_test.organizations.serializers import OrganizationShortSerializer

UserModel = get_user_model()


BASE_USER_FIELDS = [
    'email',
    'phone',
    'birthdate',
    'first_name',
    'last_name'
]


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name'
        ]


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = BASE_USER_FIELDS + [
            'password'
        ]


class UserCreateSerializer(BaseUserSerializer):
    password = serializers.CharField(required=True)

    class Meta(BaseUserSerializer.Meta):
        ...

    def create(self, validated_data):
        # make sure hashed password is set
        password = validated_data.pop('password')
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance


class UserUpdateSerializer(BaseUserSerializer):
    password = serializers.CharField(required=False, write_only=True)

    class Meta(BaseUserSerializer.Meta):
        ...

    def update(self, instance, validated_data):
        if password := validated_data.pop('password', None):
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationShortSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = BASE_USER_FIELDS + [
            'id',
            'organization',
            'date_joined',
        ]
        read_only_fields = ['date_joined']
