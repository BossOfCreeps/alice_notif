from rest_framework.response import Response
from rest_framework.views import APIView

from devices.models import Device
from devices.serializers import DeviceSerializer


class StatusView(APIView):
    def get(self, request):  # noqa
        return Response()

    def post(self, request):  # noqa
        return Response()


class DeviceListView(APIView):
    def get(self, request, *args, **kwargs):  # noqa
        return Response(
            {
                "request_id": request.headers.get("X-Request-Id"),
                "payload": {
                    "user_id": str(request.user.id),
                    "devices": DeviceSerializer(Device.objects.all(), many=True).data,
                },
            }
        )


class DeviceDetailView(APIView):
    def post(self, request, *args, **kwargs):  # noqa
        devices = Device.objects.filter(id__in=[int(d["id"]) for d in request.data.get("devices", [])])
        return Response(
            {
                "request_id": request.headers.get("X-Request-Id"),
                "payload": {
                    "devices": DeviceSerializer(Device.objects.all(), many=True).data,
                    "error_code": "",
                    "error_message": "",
                },
            }
        )


"""
{
    "request_id": "9f124dc4-c944-4256-88b2-b1b0cb778616",
    "payload": {
        "user_id": "None",
        "devices": [
            {
                "id": "1",
                "capabilities": [],
                "properties": [
                    {
                        "id": 1,
                        "name": "Влажность",
                        "type": "devices.properties.float",
                        "retrievable": true,
                        "reportable": true,
                        "parameters": {"instance": "humidity", "unit": "unit.percent"},
                    }
                ],
                "device_info": {
                    "id": 1,
                    "manufacturer": "Рога и копыта",
                    "model": "1",
                    "hw_version": "1",
                    "sw_version": "1",
                },
                "name": "увлажнитель",
                "description": "Описание",
                "type": "devices.types.humidifier",
                "room": "Комната",
                "custom_data": {},
            }
        ],
    },
}
"""
