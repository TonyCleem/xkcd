# xkcd_bot #

Отправляет случайные изображения из комикса [xkcd](https://xkcd.com) в telegram-канал.

## Установка

### Окружение

Python 3 уже должен быть установлен.
Для корректной работы скрипта рекомендую использовать все зависимости из файла `requirements.txt`
Лучше запускать с использованием виртуальной среды `venv`.

Чтобы создать `venv` и использовать скрипт, выполните следующие действия:

Создание виртуальной среды
```
python -m venv <имя venv>
```

Активация:
```
<name venv>\Scripts\activate
```

Установка всех зависимостей из `requirements.txt `
```
pip install -r requirements.txt
```
Деактивация:
```
deactivate
```
### Telegram-бот
- Создание бота с помощью [BotFather](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
- Получение [токена](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#02:~:text=%D0%B1%D0%BE%D1%82%D0%B0%2C%20%D0%B0%20%D1%82%D0%B0%D0%BA%D0%B6%D0%B5-,%D1%82%D0%BE%D0%BA%D0%B5%D0%BD,-%D0%B4%D0%BB%D1%8F%20HTTP%20API)

Укажите токен, а также имя Вашего телеграм-канала в переменных файла `.env`.

Пример файла `.env`:
>```
>TELEGRAM_TOKEN=<ваш токен бота>
>TG_CHANNEL_NAME=<имя вашего канала>
>```

## Использование

Запуск скрипта `xkcd_bot.py `:

```cmd
py xkcd_bot.py
```
Скрипт выполнит следующие действия:
- Скачает случайное изображение во временный каталог `temp_files`
- Запостит изображение из каталога в телеграм-канал
- Удалит временный каталог

## Цель проекта

Код был написан в образовательных целях в рамках онлайн-курса для веб-разработчиков [dvmn.org](https://dvmn.org/).