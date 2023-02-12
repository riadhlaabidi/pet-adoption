from django.db import models


SPECIES = ['Dog', 'Cat']
GENDER = ['Male', 'Female']
SIZES = ['Tiny', 'Small', 'Medium', 'Large']


class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(choices=SPECIES)
    breed = models.ForeignKey()  # 'pets', on_delete=
    age = models.PositiveIntegerField(min=1, max=100, blank=True, default=None)
    gender = models.CharField(choices=GENDER)
    gallery = models.ImageField()
    is_lost = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)


class Breed(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    size = models.CharField(choices=SIZES, blank=False, max_length=8)
    species = models.CharField(choices=SPECIES, blank=False, max_length=5)

    # TODO: interval from 1..5
    friendliness = models.PositiveSmallIntegerField()

    description = models.TextField()
