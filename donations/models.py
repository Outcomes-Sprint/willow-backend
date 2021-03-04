from django.db import models

# Create your models here.

class Donation(models.Model):
    name = models.TextField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    amount = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now=True)
