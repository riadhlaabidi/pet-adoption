from rest_framework import serializers
from .models import User
from apps.pets.models import Pet


class UserSerializer(serializers.ModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Pet.objects.all()
    )

    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'email',
            'phone_number',
            'birth_date',
            'is_organization',
            'pets',
        ]


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True
    )
