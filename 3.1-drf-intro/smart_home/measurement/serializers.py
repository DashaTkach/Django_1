from rest_framework import serializers
from .models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):  # 1,2 Создать и изменить датчик
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):  # 3 Добавить измерение
    class Meta:
        model = Measurement
        fields = ['id', 'temperature']


class SensorListSerializer(serializers.ModelSerializer):  # 4 Получить список датчиков
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

