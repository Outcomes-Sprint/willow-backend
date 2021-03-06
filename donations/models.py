from django.db import models
from properties.models import Property

# Create your models here.

class Donation(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=255)
    amount = models.PositiveIntegerField(blank=False, null=True)
    date = models.DateField(auto_now=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='properties', blank=False)

    def __str__(self):
        return self.amount
