from django.contrib import admin

from devices.models import Device, DeviceInfo, BaseCapability, DeviceCapability, BaseProperty, DeviceProperty


class DeviceCapabilityInline(admin.TabularInline):
    model = DeviceCapability


class DevicePropertyInline(admin.TabularInline):
    model = DeviceProperty


@admin.register(DeviceInfo)
class DeviceInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    inlines = [DeviceCapabilityInline, DevicePropertyInline]


@admin.register(BaseCapability)
class BaseCapabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(BaseProperty)
class BasePropertyAdmin(admin.ModelAdmin):
    pass
