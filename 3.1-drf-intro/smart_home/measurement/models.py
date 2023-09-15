from django.db import models


class Measurement(models.Model):
    measurement_id = models.IntegerField(primary_key=True)
    temperature = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)


class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.SlugField()

    measurements = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measurement_id')

