from django import forms

from telegram.constants import TELEGRAM_BOT_TOKEN_LEN, TELEGRAM_CHAT_ID_LEN
from telegram.models import TelegramBot, TelegramChat


class TelegramChatForm(forms.ModelForm):
    chat_id = forms.CharField(
        label="ID",
        max_length=TELEGRAM_CHAT_ID_LEN,
    )

    class Meta:
        model = TelegramChat
        fields = ("name", "chat_id")

    def clean_chat_id(self):
        value = self.cleaned_data.get("chat_id")
        if not value:
            raise forms.ValidationError("Чат ID не может быть пустым")

        return value


class TelegramBotForm(forms.ModelForm):
    api_token = forms.CharField(
        label="API токен",
        max_length=TELEGRAM_BOT_TOKEN_LEN,
    )

    class Meta:
        model = TelegramBot
        fields = ("name", "api_token", "chat")

    def clean_api_token(self):
        token = self.cleaned_data.get("api_token")
        if not token:
            raise forms.ValidationError("API токен не может быть пустым")

        return token
