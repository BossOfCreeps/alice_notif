import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.post(
            f"https://dialogs.yandex.net/api/v1/skills/{settings.SKILL_ID}/callback/state",
            headers={"Authorization": f"OAuth {settings.YANDEX_OAUTH_TOKEN}"},
            json={
                "ts": timezone.now().timestamp(),
                "payload": {
                    "user_id": "None",
                    "devices": [
                        {
                            "id": "1",
                            "capabilities": [],
                            "properties": [
                                {
                                    "type": "devices.properties.float",
                                    "state": {"instance": "humidity", "value": 10},
                                }
                            ],
                        }
                    ],
                },
            },
        )
        print(response.status_code)
        print(response.content)
