import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from scraper import scrape_url, scrape_archive

app = FastAPI()
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post('/api/archive')
async def archive(request: Request) -> JSONResponse:
    request_body = await request.json()
    date = request_body.get('date')
    topic = request_body.get('topic')
    if not date or not topic:
        raise HTTPException(status_code=400, detail='Date and topic is missing')

    day, month, year = date.split('-')
    formatted_date = f'{year}-{month}'

    url = f'https://archives.ndtv.com/articles/{formatted_date}.html'
    data = await scrape_archive(url, topic, limit=500)
    return JSONResponse(content={'content': data})

@app.post('/api/url')
async def url(request: Request) -> JSONResponse:
    request_body = await request.json()
    url = request_body.get('url')
    if not url:
        raise HTTPException(status_code=400, detail='URL is missing')

    data = await scrape_url(url)
    return JSONResponse(content={'content': data})

if __name__ == '__main__':
    uvicorn.run(app)
