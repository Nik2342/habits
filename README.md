# Трекер привычек

## Описание:
Приложение для создания полезных привычек и искоренению старых плохих привычек

## Настройка сервера:

1. Подключитесь к своему серверу:

ssh user_name@your_server_ip

2. Обновите:

sudo apt update
sudo apt upgrade

3. Настройте брандмауэр и откройте необходимые порты:

sudo ufw status
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp


## Установка:

1. Клонируйте репозиторий:
```
git@github.com
```

2. Создайте файл .env в корне проекта на основе примера .env.sample
```
Из шаблона .env.sample создайте файл .env:
SECRET_KEY =
DBENGINE =
DBNAME =
DBUSER =
DBPASSWORD =
DBHOST =
DBPORT =
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
TELEGRAM_TOKEN=
```
3. Запустите проект командой: docker-compose up --build

4. После запуска выполните миграции:docker-compose exec web python manage.py migrate


## Приложения

1. Приложение habits, в котором описана модель Habit

## Тестирование:
1. Проведены тесты для модели Habit
Тестированием покрыто 82%