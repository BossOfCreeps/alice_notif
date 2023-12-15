from django.db import models

from devices.models.devices import Device


class PropertyType(models.TextChoices):
    float = ("devices.properties.float", "float")
    event = ("devices.properties.event", "event")


class BaseProperty(models.Model):
    name = models.TextField("Название")
    type = models.CharField("Тип", choices=PropertyType, max_length=128)
    retrievable = models.BooleanField("Доступность запроса состояния")
    reportable = models.BooleanField("Признак включенного оповещения")
    parameters = models.JSONField(
        null=True, blank=True, default=dict
    )  # https://yandex.ru/dev/dialogs/smart-home/doc/concepts/properties-types.html

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"


class DeviceProperty(models.Model):
    property = models.ForeignKey(BaseProperty, models.CASCADE)
    device = models.ForeignKey(Device, models.CASCADE, "properties")
    value = models.TextField("Показатель")

    class Meta:
        verbose_name = "Свойство конкретного устройства"
        verbose_name_plural = "Свойства конкретного устройства"
