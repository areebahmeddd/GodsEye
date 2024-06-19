import httpx
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

async def scrape_archive(url: str, topic: str, limit: int) -> list:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        archive_body = soup.find('div', id='main-content')

        if archive_body:
            links = archive_body.find_all('a', href=True)
            filtered_links = [
                link['href']
                for link in links
                if topic.lower() in urlparse(link['href']).path.lower()
            ]

            return filtered_links[:limit]
        else:
            raise Exception('No archive content found.')

    except httpx.RequestError as exc:
        raise Exception(f'Error occurred: {exc}')

async def scrape_url(url: str) -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        article_body = soup.find('div', id='ins_storybody')

        if article_body:
            raw_content = article_body.get_text(strip=True)
            processed_content = re.sub(r'[^\x20-\x7E]', ' ', raw_content)
            return processed_content
        else:
            raise Exception('No article body found.')

    except httpx.RequestError as exc:
        raise Exception(f'Error occurred: {exc}')
