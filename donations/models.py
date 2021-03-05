from django.db import models

# Create your models here.

class Donation(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=255)
    amount = models.PositiveIntegerField(blank=False, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.amount
