from rest_framework.serializers import HyperlinkedModelSerializer
from .models import WeatherLocation


class WeatherLocationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = WeatherLocation
        fields = [

            "id",
            "location_name",
            "latitude",
            "longitude",

            "url" # HyperlinkedModelSerializer makes url field available
        ]