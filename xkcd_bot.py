import requests
import telegram
import os
import time
from pathlib import Path
from dotenv import load_dotenv


def get_link_from_url(url_xkcd):
    response = requests.get(url_xkcd)
    response.raise_for_status()
    comics = response.json()
    link_image = comics['img']
    return link_image


def get_coment_image(url_xkcd):
    response = requests.get(url_xkcd)
    response.raise_for_status()
    comics = response.json()
    get_coment_image = comics['alt']
    return get_coment_image


def get_title_image(url_xkcd):
    response = requests.get(url_xkcd)
    response.raise_for_status()
    comics = response.json()
    title_image = comics['title']
    return title_image


def download_image(path, link_image, title_image):
    response = requests.get(link_image)
    response.raise_for_status()
    file_path = get_file_path(path, title_image)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def send_image_with_tg_bot(path, title_image, bot, name_tg_channel):
        file_path = get_file_path(path, title_image)
        with open(file_path, 'rb') as document:
            bot.send_document(name_tg_channel, document)


def get_images_of_directory(file_path):
    directory_structure = os.walk(Path)
    for contents in directory_structure:
        dirpath, dirnames, image = contents
        return image


def get_file_path(path, title_image):
    file_name = f'{title_image}.jpg'
    file_path = path / file_name
    return file_path


def main():
    load_dotenv()
    url_xkcd = 'https://xkcd.com/info.0.json'
    tg_token = os.environ['TELEGRAM_TOKEN']
    name_tg_channel = os.environ['NAME_TG_CHANNEL']

    path = Path('./files/')
    path.mkdir(parents=True, exist_ok=True)

    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()

    while True:
        try:
            link_image = get_link_from_url(url_xkcd)
            coment_image = get_coment_image(url_xkcd)
            title_image = get_title_image(url_xkcd)
            download_image(path, link_image, title_image)
            send_image_with_tg_bot(path, title_image, bot, name_tg_channel)
            bot.send_message(chat_id=name_tg_channel, text=f'{coment_image}')
            time.sleep(86400)

        except requests.exceptions.HTTPError as error:
            print(f"Ошибка HTTP: {error}.")
            bot.send_message(chat_id=name_tg_channel, text="Сайт xkcd сегодня не доступен :sad")
            break
  

if __name__ == '__main__':
    main()




