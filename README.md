# homework_bot
Базовый Python Telegram бот с набором стандартных команд

## Функциональность

- `/start` - Приветствие и начало работы с ботом
- `/help` - Список доступных команд

## Установка и запуск с Docker

1. Склонируйте репозиторий на сервер:
```bash
git clone <repository_url>
cd work_bot
```

2. Создайте файл `.env` на основе примера:
```bash
cp env.example .env
```

3. Отредактируйте `.env` и укажите токен бота:
```
TG_TOKEN=ваш_токен_telegram_бота
```

   Токен можно получить у [@BotFather](https://t.me/BotFather) в Telegram.

4. Запустите контейнер:
```bash
docker compose up --build -d
```

## Остановка

```bash
docker compose down
```

## Переменные окружения

- `TG_TOKEN` - токен Telegram бота (обязательно)

## Локальный запуск (без Docker)

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Создайте файл `.env` с токеном:
```
TG_TOKEN=ваш_токен_telegram_бота
```

3. Запустите бота:
```bash
python work_bot.py
```
