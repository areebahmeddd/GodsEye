# Core library imports: Web scraping setup
import httpx
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Local project-specific imports: Gemini AI model
from gemini import perspec

async def ndtv_archive(url: str, topic: str, limit: int) -> list:
    try:
        # Send an asynchronous HTTP GET request to the NDTV archive URL and parse the HTML content
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        archive_body = soup.find('div', id='main-content')

        if archive_body:
            # Find all anchor tags with href attributes and filter by topic keyword
            links = archive_body.find_all('a', href=True)
            filtered_links = [
                link['href']
                for link in links
                if topic.lower() in urlparse(link['href']).path.lower()
            ]

            # Construct a list of dictionaries containing the article data for each filtered link and pass it through the Gemini AI model
            article_data = [
                {
                    'id': i + 1,
                    'content': (await ndtv_url(urlparse(link).geturl()))['content'],
                    'trending_highlights': None,
                    'trending_keywords': None,
                    'trending_organizations': None,
                    'average_positive_percentage': None,
                    'average_neutral_percentage': None,
                    'average_negative_percentage': None,
                    'total_articles': len(links),
                    'flagged_articles': None,
                    'ai_generated_articles': None
                }
                for i, link in enumerate(list(set(filtered_links))[:limit])
                # if print(f'[{i + 1}/{limit}] {link}') is None
            ]

            filtered_data = perspec(article_data)
            return filtered_data
        else:
            return [{'error': 'No archive body found'}]

    except httpx.RequestError as exc:
        return [{'error': f'Error occurred: {exc}'}]

async def ndtv_url(url: str) -> dict:
    try:
        # Send an asynchronous HTTP GET request to the NDTV article URL and parse the HTML content
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the author, date and category from the HTML content
        author_element = soup.select_one('span.pst-by_li a span[itemprop="name"]')
        author = author_element.text.strip() if author_element else None
        date_element = soup.find('span', class_='pst-by_lnk')
        date = date_element.text.strip().replace('Updated: ', '') if date_element else None
        # category_element = soup.find('a', class_='pst-by_lnk')
        # category = category_element.text.strip() if category_element else None

        # Extract the total number of ads, links, images, videos, and documents from the HTML content
        total_ads = len(soup.find_all('a', href=lambda x: x and 'adclick' in x))
        total_links = len(soup.find_all('a', href=True))
        total_images = len(soup.find_all('img'))
        total_videos = len(soup.find_all('video'))
        total_documents = len(soup.find_all('iframe'))

        # Extract the article body content from the HTML content and filter out non-ASCII characters
        article_body = soup.find('div', id='ins_storybody')
        raw_content = article_body.get_text(strip=True) if article_body else None
        filtered_content = re.sub(r'[^\x20-\x7E]', '', raw_content) if raw_content else None

        # Construct a dictionary of the extracted article data and pass it through the Gemini AI model
        article_data = {
            'publisher': 'NDTV',
            'author': author,
            'publication_date': date,
            'edited_date': date,
            'content': filtered_content,
            'authenticity': None,
            'category': None,
            'highlight': None,
            'organization': None,
            'positive_percentage': None,
            'positive_text': None,
            'neutral_percentage': None,
            'neutral_text': None,
            'negative_percentage': None,
            'negative_text': None,
            'language': None,
            'read_time': None,
            'ads': total_ads,
            'links': total_links,
            'images': total_images,
            'videos': total_videos,
            'documents': total_documents
        }

        filtered_data = perspec(article_data)
        return filtered_data

    except httpx.RequestError as exc:
        return {'error': f'Error occurred: {exc}'}
