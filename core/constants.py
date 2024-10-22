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

# Мета теги

META_TAGS_DEFAULT_LEN: int = 255
META_TAGS_AUTHOR_LEN: int = 100
META_TAGS_ROBOTS_LEN: int = 50
META_TAGS_IMAGE_URL_LEN: int = 500

META_TAG_DESCRIPTION_HELP_TEXT: str = (
    "Краткое описание сайта для "
    f"поисковых систем (не более {META_TAGS_DEFAULT_LEN} символов)"
)
META_TAG_KEYWORDS_HELP_TEXT: str = (
    "Список ключевых слов "
    "через запятую "
    f"(не более {META_TAGS_DEFAULT_LEN} символов)"
)
META_TAG_ROBOTS_HELP_TEXT: str = (
    "Настройки для поисковых систем (напр. 'index, follow' )"
)
META_TAG_AUTHOR_HELP_TEXT: str = "Имя автора или название компании"
META_TAG_OG_TITLE_HELP_TEXT: str = (
    "Заголовок для отображения в социальных сетях "
    f"(не более {META_TAGS_DEFAULT_LEN} символов)"
)

META_TAG_OG_DESCRIPTION_HELP_TEXT: str = (
    "Описание для социальных сетей "
    f"(не более {META_TAGS_DEFAULT_LEN} символов)"
)
META_TAG_OG_IMAGE_HELP_TEXT: str = (
    "URL изображения, которое будет отображаться при публикации в соц. сетях"
)
META_TAG_OG_URL_HELP_TEXT: str = "Адрес страницы для отображения в соц. сетях"
META_TAG_OG_TYPE_HELP_TEXT: str = (
    "Тип контента для Open Graph (например, 'website')"
)
META_TAG_TWITTER_CARD_HELP_TEXT: str = (
    "Тип X карточки (напр. 'summary', 'summary_large_image')"
)
META_TAG_TWITTER_TITLE_HELP_TEXT: str = (
    "Заголовок для отображения в X "
    f"(не более {META_TAGS_DEFAULT_LEN} символов)"
)
META_TAG_TWITTER_DESCRIPTION_HELP_TEXT: str = (
    "Описание для отображения в X "
    f"(не более {META_TAGS_DEFAULT_LEN} символов)"
)
META_TAG_TWITTER_IMAGE_HELP_TEXT: str = (
    "URL изображения, которое будет отображаться при публикации в X"
)
