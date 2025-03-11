from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, DueViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'dues', DueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
