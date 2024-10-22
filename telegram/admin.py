from django.contrib import admin

from telegram.constants import SHOW_ENCRYPT_DATA_LEN
from telegram.forms import TelegramBotForm, TelegramChatForm
from telegram.models import TelegramBot, TelegramChat


@admin.register(TelegramChat)
class TelegramChatAdmin(admin.ModelAdmin):
    form = TelegramChatForm
    list_display = ("name", "get_chat_id")
    list_display_links = ("name",)
    search_fields = ("name",)
    fields = ("name", "chat_id")

    def save_model(self, request, obj, form, change) -> None:
        if "chat_id" in form.cleaned_data:
            obj.chat_id = form.cleaned_data.get("chat_id")

        super().save_model(request, obj, form, change)

    def get_chat_id(self, obj) -> str:
        return f"{obj._id[:SHOW_ENCRYPT_DATA_LEN]}:***"

    get_chat_id.short_description = "ID"


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    form = TelegramBotForm
    list_display = ("name", "get_api_token")
    list_display_links = ("name",)
    search_fields = ("name",)
    fields = ("name", "api_token", "chat")

    def save_model(self, request, obj, form, change) -> None:
        if "api_token" in form.cleaned_data:
            obj.api_token = form.cleaned_data.get("api_token")

        super().save_model(request, obj, form, change)

    def get_api_token(self, obj) -> str:
        return f"{obj._api_token[:SHOW_ENCRYPT_DATA_LEN]}:***"

    get_api_token.short_description = "API токен"


admin.site.empty_value_display = "Не указано"
