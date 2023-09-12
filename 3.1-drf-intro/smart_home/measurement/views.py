# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Measurement, Sensor
from .serializers import SensorDetailSerializer


class AllView(ListAPIView):  # получаем всю информацию
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorView(RetrieveAPIView):  #  получаем информацию по конкретному объекту
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
