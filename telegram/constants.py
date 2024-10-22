TELEGRAM_CHAT_NAME_LEN: int = 60
TELEGRAM_CHAT_ID_LEN: int = 255
TELEGRAM_BOT_NAME_LEN: int = 60
TELEGRAM_BOT_TOKEN_LEN: int = 255

SHOW_ENCRYPT_DATA_LEN: int = 15

MESSAGE_TEMPLATE: str = (
    "🆕 Новое сообщение:"
    "\n\n👤 Имя: {name}"
    "\n📞 Номер телефона: {phone_number}"
    "\n📧 E-mail: {email}"
    "\n💬 Сообщение: {text}"
)

TELEGRAM_API_URL: str = "https://api.telegram.org/bot{api_token}/sendMessage"
BOT_OBJECT_CACHE_SECOND: int = 1800
