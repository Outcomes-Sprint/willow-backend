from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
# Create your views here

class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Property.objects.all()
        else:
            queryset = Property.objects.filter(user=self.request.user)

        return queryset
