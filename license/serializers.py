from rest_framework import serializers
from license.models import License
from django.contrib.auth.models import User


class LicenseSerializer(serializers.ModelSerializer):
    rented_by = serializers.ReadOnlyField(source='rented_by.username')

    class Meta:
        model = License
        fields = ('id', 'identifier', 'rented', 'rent_date', 'rented_by')


class UserSerializer(serializers.ModelSerializer):
    license = serializers.PrimaryKeyRelatedField(
        many=True, queryset=License.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')
