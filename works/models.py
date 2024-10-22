from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from core.mixins import AltTextForImageMixin, CreatedAtAndUpdatedAtMixin
from core.validators import UploadAndRenameImage
from works.constants import (
    ACHIEVEMENT_TITLE_LEN,
    ADVANTAGE_ICON_CLASS_LEN,
    ADVANTAGE_TITLE_LEN,
    EMPLOYEE_FIRST_NAME_LEN,
    EMPLOYEE_IMAGE_QUALITY_PERCENT,
    EMPLOYEE_IMAGE_SIZE,
    EMPLOYEE_LAST_NAME_LEN,
    NULL_BLANK,
    POSITION_NANE_LEN,
    REVIEW_AUTHOR_AVATAR_QUALITY_PERCENT,
    REVIEW_AUTHOR_AVATAR_SIZE,
    REVIEW_AUTHOR_NAME_LEN,
    SERVICE_PREVIEW_ALT_TEXT_LEN,
    SERVICE_PREVIEW_QUALITY_PERCENT,
    SERVICE_PREVIEW_SIZE,
    SERVICE_TITLE_LEN,
    SLIDE_IMAGE_QUALITY_PERCENT,
    SLIDE_IMAGE_SIZE,
)


class Service(CreatedAtAndUpdatedAtMixin, AltTextForImageMixin):
    title = models.CharField(
        "Название услуги",
        max_length=SERVICE_TITLE_LEN,
        unique=True,
    )
    description = models.TextField(
        "Описание",
    )
    preview = ThumbnailerImageField(
        upload_to=UploadAndRenameImage("services/"),
        resize_source=dict(
            size=SERVICE_PREVIEW_SIZE,
            sharpen=True,
            quality=SERVICE_PREVIEW_QUALITY_PERCENT,
        ),
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ("created_at",)

    @property
    def preview_alt(self) -> str:
        return self.alt_text or self.title[:SERVICE_PREVIEW_ALT_TEXT_LEN]

    def __str__(self) -> str:
        return str(self.title)


class Advantage(models.Model):
    title = models.CharField(
        "Название",
        max_length=ADVANTAGE_TITLE_LEN,
        unique=True,
    )
    icon_class = models.CharField(
        "Класс иконок",
        max_length=ADVANTAGE_ICON_CLASS_LEN,
        **NULL_BLANK,
        help_text="Подробнее -> https://getuikit.com/docs/icon#library",
    )
    description = models.TextField(
        "Описание",
    )

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = ("pk",)

    def __str__(self) -> str:
        return str(self.title)


class Slide(AltTextForImageMixin):
    image = ThumbnailerImageField(
        upload_to=UploadAndRenameImage("projects/"),
        resize_source=dict(
            size=SLIDE_IMAGE_SIZE,
            sharpen=True,
            quality=SLIDE_IMAGE_QUALITY_PERCENT,
        ),
        verbose_name="Слайд",
    )

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ("-pk",)

    @property
    def image_alt_text(self) -> str:
        return self.alt_text or self.slide_info

    @property
    def slide_info(self) -> str:
        return f"Слайд #{self.pk}"

    def __str__(self) -> str:
        return self.slide_info


class Review(CreatedAtAndUpdatedAtMixin, AltTextForImageMixin):
    author = models.CharField(
        "Имя автора",
        max_length=REVIEW_AUTHOR_NAME_LEN,
        unique=True,
    )
    author_avatar = ThumbnailerImageField(
        upload_to=UploadAndRenameImage("reviews/"),
        resize_source=dict(
            size=REVIEW_AUTHOR_AVATAR_SIZE,
            sharpen=True,
            quality=REVIEW_AUTHOR_AVATAR_QUALITY_PERCENT,
        ),
        verbose_name="Фото пользователя",
    )

    text = models.TextField(
        "Текст",
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("-created_at",)

    @property
    def author_avatar_alt_text(self) -> str:
        return self.alt_text or self.author

    def __str__(self) -> str:
        return f"Отзыв от {self.author}"


class Position(models.Model):
    name = models.CharField(
        "Название должности",
        max_length=POSITION_NANE_LEN,
        unique=True,
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ("name",)

    def __str__(self) -> str:
        return str(self.name)


class Employee(AltTextForImageMixin):
    first_name = models.CharField(
        "Имя",
        max_length=EMPLOYEE_FIRST_NAME_LEN,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=EMPLOYEE_LAST_NAME_LEN,
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Должность",
    )
    avatar = ThumbnailerImageField(
        upload_to=UploadAndRenameImage("employees/"),
        resize_source=dict(
            size=EMPLOYEE_IMAGE_SIZE,
            sharpen=True,
            quality=EMPLOYEE_IMAGE_QUALITY_PERCENT,
        ),
        verbose_name="Фото сотрудника",
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ("pk",)

    @property
    def avatar_alt_text(self) -> str:
        return self.alt_text or self.full_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name


class Achievement(models.Model):
    title = models.CharField(
        "Название",
        max_length=ACHIEVEMENT_TITLE_LEN,
        unique=True,
    )
    description = models.TextField(
        "Описание",
    )

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ("title",)

    def __str__(self) -> str:
        return str(self.title)
