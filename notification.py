import os

from discord import SyncWebhook

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
webhook = SyncWebhook.from_url(WEBHOOK_URL)


def send_notification(message: str) -> None:
    webhook.send(message)
