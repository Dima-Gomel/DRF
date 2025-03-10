from .models import Car
from .serializers import CarSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permitions import AllForAdminOtherReadOnly


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    # permission_classes = (IsAdminUser, )
    permission_classes = (AllForAdminOtherReadOnly, )

