import os
from uuid import uuid4

from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadAndRenameImage(object):
    def __init__(self, path):
        self.__sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        filename = f"{uuid4().hex}.{ext}"
        return os.path.join(self.__sub_path, filename)


class PhoneNumberRussianFormatValidator(RegexValidator):
    code = "invalid_phone_number_format"
    message = "Неверный формат российского номера телефона"
    regex = (
        r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?"
        r"[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$"
    )


class TelegramURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)?(t.me|telegram.org)\/.*$"
    code = "invalid_telegram"
    message = "Неправильный URL-адрес Telegram"


class VkontakteURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)?vk\.com\/.*$"
    code = "invalid_vkontakte"
    message = "Неправильный URL-адрес Вконтакте"


class YandexURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)?(yandex|ya)\.ru\/.*$"
    code = "invalid_yandex"
    message = "Неправильный URL-адрес Яндекс"


class InstagramURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)?instagram\.com\/.*$"
    code = "invalid_instagram"
    message = "Неправильный URL-адрес Instagram"


class YoutubeURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)?youtube\.com\/.*$"
    code = "invalid_youtube"
    message = "Неправильный URL-адрес Youtube"


class OdnoklassnikiURLValidator(RegexValidator):
    regex = r"^https:\/\/(?:www\.)?ok\.ru\/.*$"
    code = "invalid_odnoklassniki"
    message = "Неправильный URL-адрес Одноклассники"


class WhatsAppRUValidator(RegexValidator):
    regex = r"^https:\/\/wa\.me\/7\d{10}$"
    code = "invalid_whatsapp"
    message = (
        "Неправильный URL-адрес WhatsApp. Номер должен быть "
        "действительным российским номером телефона в международном "
        "формате, начинающимся с 7 и заканчивающимся 10 цифрами"
    )
