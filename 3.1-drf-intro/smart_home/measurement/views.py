from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorListSerializer


class SensorView(CreateAPIView):  # 1 Создать датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(RetrieveUpdateAPIView):  # 2 Изменить датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):  # 3 Добавить измерение
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorListCreateView(ListAPIView):  # 4 Получить список датчиков
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer
