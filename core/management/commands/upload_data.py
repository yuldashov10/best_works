import json
import os
from typing import Any, Callable

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import WebsiteMetaTag


class Command(BaseCommand):
    help = "Загрузка данных для сайта"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--file_path", type=str, help="Путь к файлу")

    def handle(self, *args, **options) -> None:
        self.process_file(
            options,
            filename="metatags_data.json",
            process_func=self.upload_meta_tags,
        )

    @staticmethod
    def get_default_file_path(filename: str) -> str:
        """Возвращает путь по умолчанию к файлу."""
        return os.path.join(settings.BASE_DIR, "data", filename)

    def process_file(
        self,
        options: dict[str, Any],
        filename: str,
        process_func: Callable,
        encoding: str = "UTF-8",
    ) -> None:
        """Общий метод для обработки файла с указанием функции."""
        file_path: str = options.get(
            "file_path"
        ) or self.get_default_file_path(filename)

        try:
            with open(file_path, mode="r", encoding=encoding) as file:
                data = json.load(file)
                process_func(data)
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f"Файл {file_path} не найден."),
            )
        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR("Ошибка при чтении JSON файла.")
            )
        except Exception as error_msg:
            self.stdout.write(
                self.style.ERROR(f"Произошла ошибка: {error_msg}")
            )

    def upload_meta_tags(self, data: dict) -> None:
        """Загружает метатегов в базу данных."""
        if WebsiteMetaTag.objects.exists():
            meta_tag = WebsiteMetaTag.objects.first()
            [setattr(meta_tag, key, value) for key, value in data.items()]
            meta_tag.save()
            msg_text: str = "Мета-теги успешно обновлены!"
        else:
            WebsiteMetaTag.objects.create(**data)
            msg_text: str = "Мета-теги успешно загружены!"

        self.stdout.write(self.style.SUCCESS(msg_text))
