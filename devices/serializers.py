from rest_framework import serializers

from devices.models import Device, DeviceInfo, BaseCapability, DeviceCapability, BaseProperty, DeviceProperty


class BaseCapabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCapability
        fields = "__all__"


class DeviceCapabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCapability
        fields = "__all__"


class BasePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProperty
        fields = "__all__"


class DevicePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceProperty
        fields = "__all__"


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    capabilities = serializers.SerializerMethodField()
    properties = serializers.SerializerMethodField()
    device_info = DeviceInfoSerializer()

    @staticmethod
    def get_capabilities(obj: Device):
        return BaseCapabilitySerializer([c.capability for c in obj.capabilities.all()], many=True).data

    @staticmethod
    def get_properties(obj: Device):
        return BasePropertySerializer([p.property for p in obj.properties.all()], many=True).data

    class Meta:
        model = Device
        fields = "__all__"
