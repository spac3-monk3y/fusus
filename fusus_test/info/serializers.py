from . import services
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class InfoSerializer(serializers.ModelSerializer):
    public_ip = serializers.SerializerMethodField()
    user_name = serializers.CharField(source='email')
    organization = serializers.CharField(
        source='organization.name',
        read_only=True
    )

    class Meta:
        model = UserModel
        fields = [
            'id',
            'user_name',
            'public_ip',
            'organization',
        ]

    def get_public_ip(self, obj):
        return services.get_public_ip()
