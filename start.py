import requests
# import telegram
import os
import pprint
from pathlib import Path
from dotenv import load_dotenv



def get_link_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    comics = response.json()
    image_url = comics['img']
    return image_url


def get_coment(url):
    response = requests.get(url)
    response.raise_for_status()

    comics = response.json()
    coment = comics['alt']
    return coment


def download_image(path, image_url):
    response = requests.get(image_url)
    response.raise_for_status()

    file_name = 'xkcd_image.jpg'
    file_path = path / file_name

    with open(file_path, 'wb') as file:
        file.write(response.content)


def send_image_with_tg_bot(bot, name_tg_channel, file_path):
        with open(file_path, 'rb') as document:
            bot.send_document(name_tg_channel, document)


def get_images_of_directory(file_path):
    directory_structure = os.walk(file_path)
    for contents in directory_structure:
        dirpath, dirnames, images = contents
        return images


def get_goups_from_vk(url_vk, vk_token):
    id_user = 143026974
    extended = 1
    version = 5.199
    headers = {
    "Authorization": f'Bearer {vk_token}'
    }
    params = {
    'user_id': id_user,
    'extended': extended,
    'v': version
    }
    response = requests.get(url_vk, headers=headers, params=params)
    response.raise_for_status()
    groups = response.json()
    return groups


def get_name_group(all_grops):
    
    name_groups = []

    groups = all_grops['response']
    name_groups = groups['items']
    for name_group in name_groups:
        name_groups.append(name_group['name'])
    return name_groups




if __name__ == '__main__':
    load_dotenv()

    url_xkcd = 'https://xkcd.com/info.0.json'
    tg_token = os.environ['TELEGRAM_TOKEN']
    vk_token = os.environ['VK_TOKEN']
    name_tg_channel = os.environ['NAME_TG_CHANNEL']

    path = Path('./Files/')
    path.mkdir(parents=True, exist_ok=True)
    images = get_images_of_directory(path)

    # bot = telegram.Bot(token=tg_token)
    # updates = bot.get_updates()

    # for image in images:
    #     file_path = path / image
    #     send_image_with_tg_bot(bot, name_tg_channel, file_path)
    #     print(f'Изображение отправлено на канал  {name_tg_channel}')



    url_vk_for_get_groups = 'https://api.vk.com/method/groups.get'
    
    url_vk = 'https://api.vk.com/method/photos.getWallUploadServer'

    all_grops = get_goups_from_vk(url_vk, vk_token)
    name_groups = get_name_group(all_grops)














    # for xkcd

    # image_url = get_link_from_url(url_xkcd)
    # download_image(path, image_url)
    # print(get_coment(url))

    

    


