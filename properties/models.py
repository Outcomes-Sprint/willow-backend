from django.db import models
from users.models import User
#from donations.models import Donation
# Create your models here.

class Property(models.Model):
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', blank=False)
    story = models.CharField(max_length=600)
    amount_needed = models.PositiveIntegerField(default=0, blank=False, null=True)
    donations = models.ForeignKey.select_related(Donation, on_delete=models.CASCADE, related_name='donations', blank=False)
    approved = models.BooleanField(null=True)
    
    def __str__(self):
        return self.address