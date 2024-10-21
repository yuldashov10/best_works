from django.contrib import admin

from core.models import (
    About,
    Address,
    Company,
    Contact,
    OpeningHour,
    SocialNetwork,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "created_at")
    list_display_links = ("name",)
    search_fields = ("email", "name", "text", "phone_number")
    fields = ("name", "phone_number", "email", "text")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
        "get_full_address",
        "get_opening_hours",
    )
    list_display_links = ("name",)
    search_fields = ("name", "phone", "email")
    fields = (
        "name",
        "phone",
        "email",
        "address",
        "opening_hours",
    )

    def get_full_address(self, obj) -> str:
        return obj.address.get_full_address

    def get_opening_hours(self, obj) -> str:
        return obj.opening_hours.get_full_opening_hour

    get_full_address.short_description = "Адрес"
    get_opening_hours.short_description = "Часы работы"


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "build")
    list_display_links = ("city",)
    list_filter = ("city",)
    search_fields = ("city", "street")
    fields = ("city", "street", "build")


@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ("weekdays", "open_time", "close_time")
    list_display_links = ("weekdays",)
    fields = ("weekdays", "open_time", "close_time")


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "icon_class", "company")
    list_display_links = ("name",)
    list_filter = ("company",)
    fields = ("company", "name", "url", "icon_class", "style_class")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("image_alt_text",)
    list_display_links = ("image_alt_text",)
    fields = (
        "image",
        "main_text",
        "sub_text",
        "alt_text",
    )


admin.site.empty_value_display = "Не указано"

admin.site.index_title = "BEST WORKS"
admin.site.site_header = "BEST WORKS | Админ-панель"
admin.site.site_title = "Управление"
