import requests
import os
from pathlib import Path


def get_link_from_url(url):
    response = requests.get(url)
    response.raise_for_status()

    images = response.json()
    image_url = images['img']
    return image_url
    
def download_image(path, image_url):
    response = requests.get(image_url)
    response.raise_for_status()

    file_name = 'xkcd_image.jpg'
    file_path = path / file_name

    with open(file_path, 'wb') as file:
        file.write(response.content)


path = Path('./images/')
path.mkdir(parents=True, exist_ok=True)

if path.exists() and path.is_dir():
    print(f"Папка успешно создана или уже существует: {path}")
else:
	print(False)


url = 'https://xkcd.com/info.0.json'

image_url = get_link_from_url(url)
download_image(path, image_url)

