from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    isManager = models.BooleanField(default=False, verbose_name='Manager')

