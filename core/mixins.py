from django.db import models

from core.constants import ALT_TEXT_LEN, NULL_BLANK


class CreatedAtAndUpdatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        "Дата создания",
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        "Дата обновления",
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class AltTextForImageMixin(models.Model):
    alt_text = models.CharField(
        "Альтернативный текст",
        max_length=ALT_TEXT_LEN,
        **NULL_BLANK,
        help_text=(
            "Для SEO-оптимизации опишите изображение кратко, "
            f"максимум {ALT_TEXT_LEN} символов"
        ),
    )

    class Meta:
        abstract = True
