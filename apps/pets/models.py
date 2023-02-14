from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


SPECIES = [('Dog', 'Dog'), ('Cat', 'Cat')]
GENDER = [('Male', 'Male'), ('Female', 'Female')]
SIZES = [('Tiny', 'Tiny'), ('Small', 'Small'),
         ('Medium', 'Medium'), ('Large', 'Large')]


class Breed(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    size = models.CharField(choices=SIZES, blank=False, max_length=8)
    species = models.CharField(choices=SPECIES, blank=False, max_length=5)
    friendliness = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=False
    )
    description = models.TextField(blank=True)


class Pet(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pets',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    species = models.CharField(choices=SPECIES, max_length=100)
    breed = models.ForeignKey(
        Breed,
        related_name='pets',
        on_delete=models.CASCADE
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        blank=True,
        default=None
    )
    gender = models.CharField(choices=GENDER, max_length=6)
    # gallery = models.ImageField()
    is_lost = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)
