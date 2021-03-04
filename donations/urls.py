from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonationViewSet, DonorViewSet

router = DefaultRouter()
router.register(r'donations', DonationViewSet, basename='donation')
router.register(r'donors', DonorViewSet, basename='donor')
urlpatterns = router.urls