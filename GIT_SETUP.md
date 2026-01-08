# Инструкция по настройке Git и пуша в репозиторий

## 1. Настройка Git репозитория (если еще не сделано)

```bash
cd /home/gaijin/bots/homework_bot_
git init
```

## 2. Добавление файлов в индекс

```bash
git add .
```

## 3. Первый коммит

```bash
git commit -m "Initial commit: базовый Telegram бот с Docker"
```

## 4. Добавление remote репозитория

Замените `<your-repo-url>` на URL вашего репозитория (GitHub, GitLab и т.д.):

```bash
# Для HTTPS
git remote add origin <your-repo-url>

# Или для SSH (если настроен ключ)
git remote add origin git@github.com:username/repo-name.git
```

## 5. Переименование ветки в main (опционально, если нужно)

```bash
git branch -M main
```

## 6. Пуш в репозиторий

```bash
# Первый пуш
git push -u origin main

# Или если ветка называется master
git push -u origin master
```

## Пример полной последовательности команд:

```bash
cd /home/gaijin/bots/homework_bot_
git init
git add .
git commit -m "Initial commit: базовый Telegram бот с Docker"
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

## Проверка статуса

```bash
git status
git remote -v  # проверить настроенные remote
```

