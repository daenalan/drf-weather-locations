from django.db import models


class WeatherLocation(models.Model):
    location_name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)

    def __str__(self):
        return self.location_name