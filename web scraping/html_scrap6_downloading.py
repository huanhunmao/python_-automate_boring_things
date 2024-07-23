import requests
import os
import bs4
import time

# 下载 xkcd 图片

url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def download_image(comic_url):
    try:
        res = requests.get(comic_url)
        res.raise_for_status()
        image_file_path = os.path.join('xkcd', os.path.basename(comic_url))
        with open(image_file_path, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
        print(f'Successfully downloaded {comic_url}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download image {comic_url}: {e}')


while not url.endswith('#'):
    try:
        # Download the page
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            download_image(comicUrl)

        # Get the Prev button's url
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')

        # Add a short delay to be polite to the server
        time.sleep(1)
    except requests.exceptions.RequestException as e:
        print(f'Failed to download page {url}: {e}')
        time.sleep(5)  # Wait before retrying

print('Done.')
