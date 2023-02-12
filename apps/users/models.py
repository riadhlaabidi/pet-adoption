from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address",
                              max_length=255,
                              unique=True)

    avatar = models.CharField()
    phone_number = models.CharField()
    birth_date = models.DateField()
    is_organization = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
