from django.urls import path

urlpatterns = [
    path('list/', AllView.as_view()),
    path('sensor/<pk>', SensorView.as_view()),
]
