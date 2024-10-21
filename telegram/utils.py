import logging
from logging import Logger

import requests
from django.core.cache import cache

from telegram.constants import (
    BOT_OBJECT_CACHE_SECOND,
    MESSAGE_TEMPLATE,
    TELEGRAM_API_URL,
)
from telegram.models import TelegramBot

logger: Logger = logging.getLogger("telegram_notifications")


def get_bot() -> TelegramBot:
    bot: TelegramBot = cache.get("bot")

    if not bot:
        bot = TelegramBot.objects.first()
        cache.set("bot", bot, BOT_OBJECT_CACHE_SECOND)

    return bot


def send_notify_to_telegram(
    name: str, phone_number: str, email: str, text: str
) -> bool:
    """Отправляет заявки пользователей в Телеграм чат."""
    bot: TelegramBot = get_bot()
    if not bot:
        logger.error("[ERROR]: Бот не найден")
        return False

    try:
        response = requests.post(
            TELEGRAM_API_URL.format(api_token=bot.api_token),
            data={
                "chat_id": bot.chat.chat_id,
                "text": MESSAGE_TEMPLATE.format(
                    name=name,
                    phone_number=phone_number,
                    email=email,
                    text=text,
                ),
            },
        )
    except Exception as error_msg:
        logger.error(f"[ERROR]: {error_msg}")
        return False

    if response.status_code == 200:
        logger.info(f"Сообщение успешно отправлено! | {name}")
        return True
    logger.error(f"[ERROR]: Ошибка при отправке: {response.status_code}")
    return False
