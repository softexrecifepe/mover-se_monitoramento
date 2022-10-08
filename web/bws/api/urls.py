from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('post_data', views.postSensorValue, name='postSensorValue'),
]
