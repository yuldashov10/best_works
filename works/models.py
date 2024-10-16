from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from core.models import CreatedAtAndUpdatedAtMixin
from works.constants import (
    NULL_BLANK,
    SERVICE_PREVIEW_ALT_TEXT_LEN,
    SERVICE_PREVIEW_QUALITY_PERCENT,
    SERVICE_PREVIEW_SIZE,
    SERVICE_TITLE_LEN,
)


class Service(CreatedAtAndUpdatedAtMixin):
    title = models.CharField(
        "Название услуги",
        max_length=SERVICE_TITLE_LEN,
        unique=True,
    )
    description = models.TextField(
        "Описание",
    )
    preview = ThumbnailerImageField(
        upload_to="services/",
        resize_source=dict(
            size=SERVICE_PREVIEW_SIZE,
            sharpen=True,
            quality=SERVICE_PREVIEW_QUALITY_PERCENT,
        ),
        verbose_name="Изображение",
        **NULL_BLANK,
    )
    preview_alt_text = models.CharField(
        "Альтернативный текст",
        max_length=SERVICE_PREVIEW_ALT_TEXT_LEN,
        **NULL_BLANK,
    )

    @property
    def preview_alt(self) -> str:
        return str(self.preview_alt_text) or str(
            self.title[:SERVICE_PREVIEW_ALT_TEXT_LEN]
        )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return str(self.title)
