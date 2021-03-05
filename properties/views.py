from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Property
from .serializers import PropertySerializer
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsOwner
# Create your views here

class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get_queryset(self, *args, **kwargs):
        return Property.objects.all()

    def perform_create(self, serializer):
        serializer.save()