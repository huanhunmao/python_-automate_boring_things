import requests
import os
import bs4
import time

# 下载 unsplash 图片
url = 'https://unsplash.com/'  # 起始 URL
os.makedirs('unsplash', exist_ok=True)  # 在 ./unsplash 目录中存储图片


def download_image(image_url):
    try:
        res = requests.get(image_url)
        res.raise_for_status()

        # 确认响应头的内容类型是图片
        if 'image' in res.headers.get('Content-Type', ''):
            image_file_path = os.path.join('unsplash',
                                           os.path.basename(image_url))
            with open(image_file_path, 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
            print(f'Successfully downloaded {image_url}')
        else:
            print(f'The URL did not point to an image: {image_url}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download image {image_url}: {e}')


while not url.endswith('#'):
    try:
        # 下载页面
        print(f'Downloading page {url}...')
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # 查找图片 URL
        comic_elem = soup.select('img[class="ApbSI z1piP vkrMA"]')
        if not comic_elem:
            print('Could not find comic image.')
        else:
            image_url = comic_elem[0].get('src')
            if image_url.startswith('//'):
                image_url = 'https:' + image_url
            download_image(image_url)

        # 获取“上一页”按钮的 URL
        prev_link = soup.select('a[class="Prxeh"]')
        if prev_link:
            url = 'https://unsplash.com' + prev_link[0].get('href')
        else:
            print('Could not find previous link.')
            break

        # 添加短暂延迟，以礼貌对待服务器
        time.sleep(1)
    except requests.exceptions.RequestException as e:
        print(f'Failed to download page {url}: {e}')
        time.sleep(5)  # 重试前等待

print('Done.')
