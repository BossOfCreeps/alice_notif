from django.db import models


class DeviceInfo(models.Model):
    manufacturer = models.TextField()
    model = models.TextField()
    hw_version = models.TextField()
    sw_version = models.TextField()

    class Meta:
        verbose_name = "Информация об устройстве"
        verbose_name_plural = "Информация об устройствах"


class Device(models.Model):
    name = models.TextField("Имя")
    description = models.TextField("Описание")
    type = models.TextField("Тип устройства")  # https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html
    room = models.TextField("Комната")
    custom_data = models.JSONField(null=True, blank=True, default=dict)
    device_info = models.ForeignKey(DeviceInfo, models.PROTECT, "devices")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"
