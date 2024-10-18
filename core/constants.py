from typing import Callable

from core.validators import (
    InstagramURLValidator,
    OdnoklassnikiURLValidator,
    TelegramURLValidator,
    VkontakteURLValidator,
    WhatsAppRUValidator,
    YandexURLValidator,
    YoutubeURLValidator,
)

USER_NAME_LEN: int = 60

SOCIAL_NETWORK_NAME_LEN: int = 30
SOCIAL_NETWORK_URL_LEN: int = 255
SOCIAL_NETWORK_ICON_CLASS_LEN: int = 255

SOCIAL_NETWORK_CHOICES: tuple[tuple[str, str], ...] = (
    ("telegram", "Telegram"),
    ("vkontakte", "Вконтакте"),
    ("yandex", "Яндекс"),
    ("instagram", "Instagram"),
    ("youtube", "YouTube"),
    ("odnoklassniki", "Одноклассники"),
    ("whatsapp", "Whatsapp"),
)

SOCIAL_NETWORK_VALIDATORS: dict[str, Callable] = {
    "telegram": TelegramURLValidator(),
    "vkontakte": VkontakteURLValidator(),
    "yandex": YandexURLValidator(),
    "instagram": InstagramURLValidator(),
    "youtube": YoutubeURLValidator(),
    "odnoklassniki": OdnoklassnikiURLValidator(),
    "whatsapp": WhatsAppRUValidator(),
}

CITY_NAME_LEN: int = 60
STREET_NAME_LEN: int = 60
BUILDING_NAME_LEN: int = 30

COMPANY_NAME_LEN: int = 60
COMPANY_PHONE_NUMBER_LEN: int = 30
WEEKDAYS_LEN: int = 30

NULL_BLANK: dict[str, bool] = {
    "null": True,
    "blank": True,
}
ABOUT_IMAGE_SIZE: tuple[int, int] = (1280, 720)
ABOUT_IMAGE_QUALITY_PERCENT: int = 95

ALT_TEXT_LEN: int = 20
