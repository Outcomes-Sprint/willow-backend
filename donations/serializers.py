from rest_framework import serializers
from .models import Donation, Donor

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('date')

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ('name', 'email')