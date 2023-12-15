from django.urls import path

from devices.views import StatusView, DeviceListView

urlpatterns = [
    path("", StatusView.as_view(), name="status"),
    path("user/devices", DeviceListView.as_view(), name="devices"),
]
