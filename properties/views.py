from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Property
from .serializers import PropertySerializer
from donations.serializers import DonationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import IsOwner
from rest_framework import status
# Create your views here


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Property.objects.all()
        else:
            queryset = Property.objects.filter(user=self.request.user)

        return queryset

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # @action(detail=True, methods=['post'])
    # def make_donation(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = DonationSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         user.make_donation(serializer.data['amount'])
    #         user.save()
    #         return Response({'status': 'donation successsful'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def list(self, request):
    #     pass
    # def create(self, request):
    #     pass
    # def retrieve(self, request, pk=None):
    #     pass
    # def update(self, request, pk=None):
    #     pass
    # def partial_update(self, request, pk=None):
    #     pass
    # def destroy(self, request, pk=None):
    #     pass