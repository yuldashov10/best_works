from cryptography.fernet import Fernet
from django.conf import settings


class CipherManager:
    """Менеджер шифрования."""

    def __init__(self, cipher_key: str | None = None) -> None:
        """Инициализация менеджера шифрования.
        Если ключ не передан, используется ключ из настроек."""
        self.__cipher_key = cipher_key or settings.SECRET_CIPHER_KEY
        self.__cipher = Fernet(self.__cipher_key)
        self.__encoding = "UTF-8"

    @staticmethod
    def generate_key() -> str:
        """Генерация нового ключа шифрования.
        Вызывается однократно для создания ключа."""
        return Fernet.generate_key().decode()

    def encrypt(self, data: str) -> str:
        """Шифрование данных."""
        return self.__cipher.encrypt(
            data.encode(encoding=self.__encoding)
        ).decode(encoding=self.__encoding)

    def decrypt(self, data: str) -> str:
        """Дешифрование данных."""
        return self.__cipher.decrypt(
            data.encode(encoding=self.__encoding)
        ).decode(encoding=self.__encoding)


if __name__ == "__main__":
    cipher = CipherManager()
    print(cipher.generate_key())
