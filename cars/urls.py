from django.urls import path, include
from rest_framework import routers
from . views import CarViewSet

router = routers.DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
