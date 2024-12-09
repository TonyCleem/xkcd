import requests
import telegram
import os
import random
import shutil
from pathlib import Path
from dotenv import load_dotenv


def get_image_from_xkcd(xkcd_url):
    response = requests.get(xkcd_url)
    response.raise_for_status()
    comics = response.json()
    image_link = comics['img']
    image_title = comics['title']
    image_coment = comics['alt']
    image_num = comics['num']
    image = image_link, image_title, image_coment, image_num
    return image


def download_image(path, image_link, image_title):
    response = requests.get(image_link)
    response.raise_for_status()
    file_path = get_file_path(path, image_title)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def send_image_with_tg_bot(path, image_title, bot, tg_channel_name):
        file_path = get_file_path(path, image_title)
        with open(file_path, 'rb') as document:
            bot.send_document(tg_channel_name, document)


def get_images_of_directory(file_path):
    directory_structure = os.walk(Path)
    for contents in directory_structure:
        dirpath, dirnames, image = contents
        return image


def get_file_path(path, image_title):
    file_name = f'{image_title}.jpg'
    file_path = Path(path, file_name)
    return file_path


def main():
    load_dotenv()
    xkcd_url = 'https://xkcd.com/info.0.json'
    tg_token = os.environ['TELEGRAM_TOKEN']
    tg_channel_name = os.environ['TG_CHANNEL_NAME']

    path = Path('temp_files')
    path.mkdir(parents=True, exist_ok=True)

    try:
        bot = telegram.Bot(token=tg_token)
        updates = bot.get_updates()
    
        image = get_image_from_xkcd(xkcd_url)
        image_link, image_title, image_coment, image_num = image
        number_comics = random.randint(1, int(image_num))
    
        new_xkcd_url = f'https://xkcd.com/{number_comics}/info.0.json'
        image = get_image_from_xkcd(new_xkcd_url)
        image_link, image_title, image_coment, image_num = image
        download_image(path, image_link, image_title)
        send_image_with_tg_bot(path, image_title, bot, tg_channel_name)
        bot.send_message(chat_id=tg_channel_name, text=f'{image_coment}')
    finally:
        shutil.rmtree(path)


if __name__ == '__main__':
    main()




