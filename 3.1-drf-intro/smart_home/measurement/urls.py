from django.urls import path
from .views import SensorView, SensorListCreateView, SensorUpdateView, MeasurementView

urlpatterns = [
    path('sensor_create/', SensorView.as_view()),
    path('sensor_update/', SensorUpdateView.as_view()),
    path('measurement_create/', MeasurementView.as_view()),
    path('sensor_list/', SensorListCreateView.as_view()),
]
