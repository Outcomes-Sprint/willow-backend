from django.db import models
from users.models import User

# Create your models here.

class Property(models.Model):
    address = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', blank=False)
    story = models.CharField(max_length=600)
    amount_needed = models.PositiveIntegerField(default=0, blank=False, null=True)
    monthly_payment = models.PositiveIntegerField(default=0, blank=False, null=True)
    missed_payments = models.PositiveIntegerField(default=0, blank=False, null=True)
    approved = models.BooleanField(null=True)
    documentation = models.FileField(upload_to='documents/', null=True, blank=True) 
    
    PRE_FORECLOSURE = 'Pre-Foreclosure'
    PHASE_1 = 'Payment Default'
    PHASE_2 = 'Notice of Default'
    PHASE_3 = "Notice of Trustee's Sale"
    PHASE_4 = "Trustee's Sale"
    PHASE_5 = 'Real Estate Owned(REO)'
    PHASE_6 = 'Eviction' 

    PRIORITY_OPTIONS = [
        (PRE_FORECLOSURE, 'Pre-Foreclosure'),
        (PHASE_1, 'Payment Default'),
        (PHASE_2, 'Notice of Default'),
        (PHASE_3, "Notice of Trustee's Sale"),
        (PHASE_4, "Trustee's Sale"),
        (PHASE_5, 'Real Estate Owned(REO)'),
        (PHASE_6, 'Eviction'),
    ]
    foreclosure_status = models.CharField(
        max_length=30,
        choices=PRIORITY_OPTIONS,
        default=PRE_FORECLOSURE,
    )

    def __str__(self):
        return self.address