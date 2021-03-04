from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .models import Donation, Donor
from .serializers import DonationSerializer, DonorSerializer
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


class DonorViewSet(viewsets.ModelViewSet):
    serializer_class = DonorSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Donor.objects.all()
        else:
            queryset = Donor.objects.filter(user=self.request.user)

        return queryset
