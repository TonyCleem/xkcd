# xkcd_bot #

Sends daily fresh pictures from the comic [xkcd](https://xkcd.com) in the telegram channel.

## Installation

### Environment

Python 3 should already be installed.
For the script to work correctly, I recommend using all the dependencies from the file `requirements.txt `
It is better to launch using the virtual environment `venv`.

To create a `venv` and use the script, follow these steps:


Creating a virtual environment
```
python -m venv <name venv>
```

Activate:
```
<name venv>\Scripts\activate
```

Installing all dependencies from `requirements.txt `
```
pip install -r requirements.txt
```
Deactivate the script at the end of the work
```
deactivate
```

### Telegram bot
- Creating a bot via [BotFather](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
- Get the [token](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#02:~:text=%D0%B1%D0%BE%D1%82%D0%B0%2C%20%D0%B0%20%D1%82%D0%B0%D0%BA%D0%B6%D0%B5-,%D1%82%D0%BE%D0%BA%D0%B5%D0%BD,-%D0%B4%D0%BB%D1%8F%20HTTP%20API)

Specify the received token in the variables of the `.env` file.

Example of the `.env` file:
>```
>TELEGRAM_TOKEN=<token from your bot>
>```

## Usage

Running the script `xkcd_bot.py `

If there are problems with the site [xkcd](https://xkcd.com) the script will return an exception and stop working. After restoring the site, run the script again

## The purpose of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).