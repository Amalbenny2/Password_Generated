from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=70, blank=True, unique=True)
    # other fields and methods for your CustomUser model
