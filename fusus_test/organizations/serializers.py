from .models import Organization
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = [
            'id',
            'name'
        ]
        read_only_fields = ['id', 'name']
