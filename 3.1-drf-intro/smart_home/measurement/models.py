from django.db import models


class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.SlugField()


class Measurement(models.Model):
    measurement_id = models.IntegerField(primary_key=True)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    sensor = models.ForeignKey(Sensor, models.CASCADE, related_name='measurements', default=True)

