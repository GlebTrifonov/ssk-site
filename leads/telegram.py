import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_telegram_message(text):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    if token == "" or chat_id == "":
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        response = requests.post(
            url, json={"chat_id": chat_id, "text": text}, timeout=5
        )
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Не удалось отправить сообщение в Telegram")
