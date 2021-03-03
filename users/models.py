from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    approved = models.BooleanField(default=False)

