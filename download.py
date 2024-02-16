#!/usr/bin/env python3

from urllib.parse import urljoin
import os
import requests

def download():
    os.makedirs('downloads', exist_ok=True)

    downloads_max = -1
    downloads = 0

    with open('index.txt', 'r') as index:
        for sub in index:
            if downloads == downloads_max:
                break

            url = urljoin('https://www.cia.gov/library/abbottabad-compound/', sub.strip())

            response = requests.get(url)

            if response.status_code != 200:
                print(f'{response.status_code}: {url}')
                continue

            with open(os.path.join('downloads', os.path.basename(sub.strip())), 'wb') as file:
                file.write(response.content)

            downloads += 1

if __name__ == '__main__':
    download()
