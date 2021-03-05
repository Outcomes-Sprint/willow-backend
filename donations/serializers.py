from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    # date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Donation
        fields = ('name', 'email', 'amount')