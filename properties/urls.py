from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProperyViewSet

router = DefaultRouter()
router.register(r'properties', ProperyViewSet, basename='property')
urlpatterns = router.urls