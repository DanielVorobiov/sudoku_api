from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(blank=True, null=True, max_length=100)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    username = None
    is_staff = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
