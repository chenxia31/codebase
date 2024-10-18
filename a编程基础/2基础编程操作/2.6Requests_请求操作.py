import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def download_pdfs_from_page(url, save_folder):
    # 创建保存 PDF 的文件夹
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # 获取网页内容
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功

    # 解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找所有的 PDF 链接
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.lower().endswith('.pdf'):
            full_url = urljoin(url, href)
            pdf_links.append(full_url)

    print(f'在页面中发现了 {len(pdf_links)} 个 PDF 文件。')

    # 下载每个 PDF 文件
    for pdf_url in pdf_links:
        try:
            pdf_response = requests.get(pdf_url)
            pdf_response.raise_for_status()

            # 从 URL 中获取文件名
            parsed_url = urlparse(pdf_url)
            pdf_name = os.path.basename(parsed_url.path)

            # 保存 PDF 文件
            pdf_path = os.path.join(save_folder, pdf_name)
            with open(pdf_path, 'wb') as f:
                f.write(pdf_response.content)
            print(f'已下载：{pdf_name}')
        except requests.exceptions.RequestException as e:
            print(f'下载失败：{pdf_url}\n错误信息：{e}')

    print('所有 PDF 文件下载完成。')

if __name__ == '__main__':
    page_url = 'https://cs61a.org/'  # 替换为您要下载的网页 URL
    save_directory = 'downloaded_pdfs'  # 指定保存 PDF 的文件夹

    download_pdfs_from_page(page_url, save_directory)
