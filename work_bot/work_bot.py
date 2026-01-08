import logging
import os
import sys
from dotenv import load_dotenv
from telebot import TeleBot
from telebot import types

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TG_TOKEN')

if not TELEGRAM_TOKEN:
    logging.critical('Отсутствует переменная окружения: TG_TOKEN')
    raise ValueError('Отсутствует переменная окружения: TG_TOKEN')

# Создаем объект бота
bot = TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start"""
    bot.reply_to(
        message,
        f"Привет, {message.from_user.first_name}!\n"
    )
    logging.info(f"Пользователь {message.from_user.id} использовал команду /start")


@bot.message_handler(commands=['help'])
def send_help(message):
    """Обработчик команды /help"""
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение\n"
        "/echo <текст> - Повторить ваш текст\n"
        "\n"
        "Также вы можете просто написать мне сообщение, и я его повторю."
    )
    bot.reply_to(message, help_text)
    logging.info(f"Пользователь {message.from_user.id} использовал команду /help")


@bot.message_handler(commands=['echo'])
def echo_command(message):
    """Обработчик команды /echo"""
    text = message.text.split(' ', 1)
    if len(text) > 1:
        bot.reply_to(message, text[1])
        logging.info(f"Пользователь {message.from_user.id} использовал команду /echo")
    else:
        bot.reply_to(message, "Использование: /echo <текст>")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Обработчик всех остальных сообщений"""
    bot.reply_to(message, message.text)
    logging.info(f"Пользователь {message.from_user.id} отправил сообщение: {message.text}")


def main():
    """Основная логика работы бота."""
    logging.info("Бот запущен и готов к работе")
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as error:
        logging.exception(f"Ошибка в работе бота: {error}")
        raise


if __name__ == '__main__':
    # Настройки логирования
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler('main.log', mode='a', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    # Запуск основной функции
    main()
