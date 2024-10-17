from django.db import models

from core.constants import USER_NAME_LEN
from core.mixins import CreatedAtAndUpdatedAtMixin


class Contact(CreatedAtAndUpdatedAtMixin):
    name = models.CharField(
        "Ваше Имя",
        max_length=USER_NAME_LEN,
    )
    email = models.EmailField(
        "Ваш адрес электронной почты",
    )
    text = models.TextField(
        "Сообщение",
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return str(self.name)


class SocialNetwork(models.Model):
    pass
