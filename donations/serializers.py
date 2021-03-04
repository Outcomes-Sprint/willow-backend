from rest_framework import serializers
from .models import Donation, Donor

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('name', 'email', 'amount','date')