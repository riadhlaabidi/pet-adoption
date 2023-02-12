from rest_framework import serializers
from .models import Breed, Pet


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            'id',
            'name',
            'size',
            'species',
            'friendliness',
            'description'
        ]


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
