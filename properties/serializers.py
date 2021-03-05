from rest_framework import serializers
from .models import Property
from donations.models import Donation

class PropertySerializer(serializers.ModelSerializer):
    approved = serializers.ReadOnlyField(
        source='property.approved',
        read_only=True
    )
    donations = serializers.ReadOnlyField(
        source='donation.amount',
        read_only=True
    )
    class Meta:
        model = Property
        fields = ('address', 'user', 'story', 'amount_needed', 'donations', 'approved')