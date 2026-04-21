from rest_framework import viewsets, permissions
from .serializers import WeatherLocationSerializer
from .models import WeatherLocation


class WeatherLocationViewSet(viewsets.ModelViewSet):
    queryset = WeatherLocation.objects.all()
    serializer_class = WeatherLocationSerializer
    permission_classes = [permissions.IsAuthenticated]