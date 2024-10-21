from typing import Callable

from django.core.exceptions import ValidationError
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from core.constants import (
    ABOUT_IMAGE_QUALITY_PERCENT,
    ABOUT_IMAGE_SIZE,
    BUILDING_NAME_LEN,
    CITY_NAME_LEN,
    COMPANY_NAME_LEN,
    COMPANY_PHONE_NUMBER_LEN,
    NULL_BLANK,
    SOCIAL_NETWORK_CHOICES,
    SOCIAL_NETWORK_ICON_CLASS_LEN,
    SOCIAL_NETWORK_NAME_LEN,
    SOCIAL_NETWORK_URL_LEN,
    SOCIAL_NETWORK_VALIDATORS,
    STREET_NAME_LEN,
    USER_NAME_LEN,
    WEEKDAYS_LEN,
)
from core.mixins import AltTextForImageMixin, CreatedAtAndUpdatedAtMixin
from core.validators import (
    PhoneNumberRussianFormatValidator,
    UploadAndRenameImage,
)


class Contact(CreatedAtAndUpdatedAtMixin):
    name = models.CharField(
        "Ваше Имя",
        max_length=USER_NAME_LEN,
    )
    phone_number = models.CharField(
        "Ваш номер телефона",
        max_length=COMPANY_PHONE_NUMBER_LEN,
        validators=[PhoneNumberRussianFormatValidator()],
    )
    email = models.EmailField(
        "Ваш адрес электронной почты",
    )
    text = models.TextField(
        "Сообщение",
    )

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return str(self.name)


class Company(models.Model):
    name = models.CharField(
        "Название",
        max_length=COMPANY_NAME_LEN,
        unique=True,
    )
    phone = models.CharField(
        "Номер телефона",
        max_length=COMPANY_PHONE_NUMBER_LEN,
        validators=[PhoneNumberRussianFormatValidator()],
    )
    email = models.EmailField(
        "Электронная почта",
    )
    address = models.OneToOneField(
        "Address",
        on_delete=models.CASCADE,
        related_name="company",
        verbose_name="Адрес компании",
    )
    opening_hours = models.OneToOneField(
        "OpeningHour",
        on_delete=models.CASCADE,
        related_name="company",
        verbose_name="Часы работы компании",
    )

    constraints = [
        models.UniqueConstraint(
            fields=("city", "street", "build"),
            name="invalid_company_phone_unique",
        )
    ]

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self) -> str:
        return str(self.name)


class SocialNetwork(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="social_networks",
        verbose_name="Компания",
    )
    name = models.CharField(
        "Социальная сеть",
        max_length=SOCIAL_NETWORK_NAME_LEN,
        choices=SOCIAL_NETWORK_CHOICES,
        unique=True,
    )
    url = models.URLField(
        "URL-адрес",
        max_length=SOCIAL_NETWORK_URL_LEN,
        unique=True,
        help_text=(
            "Например: https://wa.me/phone_number, "
            "https://t.me/username или https://vk.com/username"
        ),
    )
    icon_class = models.CharField(
        "Класс иконок",
        max_length=SOCIAL_NETWORK_ICON_CLASS_LEN,
        blank=True,
        help_text=(
            "Укажите UIkit CSS-класс для "
            "значка -> https://getuikit.com/docs/icon#library"
        ),
    )
    style_class = models.CharField(
        "Класс иконок",
        max_length=SOCIAL_NETWORK_ICON_CLASS_LEN,
        **NULL_BLANK,
        help_text="Здесь Вы можете перечислить UIkit CSS-классы через пробел",
    )

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"
        ordering = ("name",)

    def clean(self) -> None:
        validator: Callable = SOCIAL_NETWORK_VALIDATORS.get(str(self.name))
        if validator:
            validator(self.url)

        if self.url and not self.icon_class:
            raise ValidationError("Необходимо указать класс значка")
        if self.icon_class and not self.url:
            raise ValidationError("Необходимо указать URL")

    def __str__(self) -> str:
        return self.get_name_display()


class Address(models.Model):
    city = models.CharField(
        "Город",
        max_length=CITY_NAME_LEN,
    )
    street = models.CharField(
        "Улица",
        max_length=STREET_NAME_LEN,
    )
    build = models.CharField(
        "Дом, здание",
        max_length=BUILDING_NAME_LEN,
    )

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        ordering = ("city",)
        constraints = [
            models.UniqueConstraint(
                fields=("city", "street", "build"),
                name="invalid_address_unique",
            )
        ]

    @property
    def get_full_address(self) -> str:
        return f"г.{self.city}, ул.{self.street}, д.{self.build}"

    def __str__(self) -> str:
        return f"{self.city}, {self.street}, {self.build}"


class OpeningHour(models.Model):
    weekdays = models.CharField(
        "Дни недели",
        max_length=WEEKDAYS_LEN,
        unique=True,
    )
    open_time = models.TimeField("С")
    close_time = models.TimeField("До")

    class Meta:
        verbose_name = "Режим работы"
        verbose_name_plural = "Режим работы"
        ordering = ("weekdays",)

    def __get_hours_and_minutes(self, value: models.TimeField) -> str:
        return value.strftime("%H:%M")

    @property
    def get_full_opening_hour(self) -> str:
        return (
            f"{self.weekdays}: "
            f"{self.__get_hours_and_minutes(self.open_time)} — "
            f"{self.__get_hours_and_minutes(self.close_time)}"
        )

    def __str__(self) -> str:
        return str(self.weekdays)


class About(AltTextForImageMixin):
    image = ThumbnailerImageField(
        upload_to=UploadAndRenameImage("projects/"),
        resize_source=dict(
            size=ABOUT_IMAGE_SIZE,
            sharpen=True,
            quality=ABOUT_IMAGE_QUALITY_PERCENT,
        ),
        verbose_name="Изображение",
    )
    main_text = models.TextField(
        "Основной текст о нас",
    )
    sub_text = models.TextField(
        "Дополнительный текст о нас",
        **NULL_BLANK,
    )

    class Meta:
        verbose_name = "Страница о нас"
        verbose_name_plural = "Страница о нас"
        ordering = ("-pk",)

    @property
    def image_alt_text(self) -> str:
        return self.alt_text or f"Картинка #{self.pk}"

    def __str__(self) -> str:
        return f"О нас информация #{self.pk}"
