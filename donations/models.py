from django.db import models

# Create your models here.

class Donation(models.Model):
    date = models.DateField(auto_now=True)
    # amount = models.PositiveIntegerField()
    # userID -> ObjectID


class Donor(models.Model):
    name = models.TextField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    # donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name='donors', blank=False)
