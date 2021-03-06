from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    approved = serializers.ReadOnlyField(
        source='property.approved',
        read_only=True
    )
   
    class Meta:
        model = Property
        fields = ('address', 'owner','user', 'story', 'amount_needed','monthly_payment','missed_payments', 'approved', 'documentation', 'foreclosure_status')