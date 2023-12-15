from django.db import models

from devices.models.devices import Device


class CapabilityType(models.TextChoices):
    on_off = ("devices.capabilities.on_off", "on_off")
    color_setting = ("devices.capabilities.color_setting", "color_setting")
    mode = ("devices.capabilities.mode", "mode")
    range = ("devices.capabilities.range", "range")
    toggle = ("devices.capabilities.toggle", "toggle")


class BaseCapability(models.Model):
    name = models.TextField("Название")
    type = models.CharField("Тип", choices=CapabilityType, max_length=128)
    retrievable = models.BooleanField("Доступность запроса состояния")
    reportable = models.BooleanField("Признак включенного оповещения")
    parameters = models.JSONField(
        null=True, blank=True, default=dict
    )  # https://yandex.ru/dev/dialogs/smart-home/doc/concepts/capability-types.html

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Умение"
        verbose_name_plural = "Умения"


class DeviceCapability(models.Model):
    capability = models.ForeignKey(BaseCapability, models.CASCADE)
    device = models.ForeignKey(Device, models.CASCADE, "capabilities")
    value = models.TextField("Показатель")

    class Meta:
        verbose_name = "Умение конкретного устройства"
        verbose_name_plural = "Умения конкретного устройства"
