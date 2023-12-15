from rest_framework.response import Response
from rest_framework.views import APIView

from devices.models import Device
from devices.serializers import DeviceSerializer


class StatusView(APIView):
    def get(self, request):  # noqa
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
