from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, MembershipTypeViewSet

# Create a router and register the viewsets
router = DefaultRouter()

# Register MemberViewSet
router.register(r'members', MemberViewSet, basename='member')

# Register MembershipTypeViewSet
router.register(r'membershipTypes', MembershipTypeViewSet, basename='membership-type')

urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),
]