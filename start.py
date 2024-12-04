import requests
import os
from pathlib import Path


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


path = Path('./Files/')
path.mkdir(parents=True, exist_ok=True)

url = 'https://xkcd.com/info.0.json'

image_url = get_link_from_url(url)
download_image(path, image_url)
print(get_coment(url))

