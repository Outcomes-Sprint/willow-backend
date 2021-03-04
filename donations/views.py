from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .models import Donation
from .serializers import DonationSerializer
from .permissions import IsOwner


class DonationViewSet(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Donation.objects.all()
        else:
            queryset = Donation.objects.filter(user=self.request.user)

        return queryset