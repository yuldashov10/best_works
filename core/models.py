from django.db import models


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
