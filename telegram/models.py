from django.db import models

from core.mixins import CreatedAtAndUpdatedAtMixin
from telegram.constants import (
    TELEGRAM_BOT_NAME_LEN,
    TELEGRAM_BOT_TOKEN_LEN,
    TELEGRAM_CHAT_ID_LEN,
    TELEGRAM_CHAT_NAME_LEN,
)
from telegram.enryption_utils import CipherManager


class TelegramChat(CreatedAtAndUpdatedAtMixin):
    name = models.CharField(
        "Название",
        max_length=TELEGRAM_CHAT_NAME_LEN,
        unique=True,
    )
    _id = models.CharField(
        "ID",
        max_length=TELEGRAM_CHAT_ID_LEN,
        unique=True,
        editable=False,
    )

    cipher = CipherManager()

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
        ordering = ("-created_at",)

    @property
    def chat_id(self) -> str:
        """Декодирует чат ID при доступе."""
        return self.cipher.decrypt(str(self._id))

    @chat_id.setter
    def chat_id(self, value: str) -> None:
        """Шифрует чат ID перед сохранением."""
        if not value:
            raise ValueError("Чат ID не может быть пустым")

        self._id = self.cipher.encrypt(value)

    def __str__(self) -> str:
        return str(self.name)


class TelegramBot(CreatedAtAndUpdatedAtMixin):
    name = models.CharField(
        "Название",
        max_length=TELEGRAM_BOT_NAME_LEN,
        unique=True,
    )
    _api_token = models.CharField(
        "API токен",
        max_length=TELEGRAM_BOT_TOKEN_LEN,
        editable=False,
    )
    chat = models.OneToOneField(
        TelegramChat,
        on_delete=models.CASCADE,
        verbose_name="Чат",
    )

    cipher = CipherManager()

    class Meta:
        verbose_name = "Бот"
        verbose_name_plural = "Боты"
        ordering = ("-created_at",)

    @property
    def api_token(self) -> str:
        """Декодирует токен при доступе."""
        return self.cipher.decrypt(str(self._api_token))

    @api_token.setter
    def api_token(self, value: str) -> None:
        """Шифрует токен перед сохранением."""
        if not value:
            raise ValueError("API токен не может быть пустым")

        self._api_token = self.cipher.encrypt(value)

    def __str__(self) -> str:
        return f"{self.name} | {self.chat.name}"
