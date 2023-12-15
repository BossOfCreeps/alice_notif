from django.urls import path

from devices.views import StatusView, DeviceListView, DeviceDetailView

urlpatterns = [
    path("", StatusView.as_view(), name="status"),
    path("user/unlink", StatusView.as_view(), name="unlink"),
    path("user/devices", DeviceListView.as_view(), name="devices"),
    path("user/devices/query", DeviceDetailView.as_view(), name="query"),
    path("user/devices/action", StatusView.as_view(), name="action"),
]
