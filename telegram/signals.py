from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Contact
from telegram.utils import send_notify_to_telegram


@receiver(post_save, sender=Contact)
def send_notify(sender, instance, created, **kwargs) -> None:
    send_notify_to_telegram(
        instance.name,
        instance.phone_number,
        instance.email,
        instance.text,
    )
