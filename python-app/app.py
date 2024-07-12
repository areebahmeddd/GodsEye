# Core library imports: FastAPI setup
import uvicorn
import subprocess
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Local project-specific imports: custom scraper and database functions
from scraper import ndtv_archive, ndtv_url
# from database import database_history

app = FastAPI() # Initialize FastAPI application instance
# Configure CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post('/api/archive')
async def archive(request: Request) -> JSONResponse:
    # Get source, date, and topic values from the incoming JSON data
    request_body = await request.json()
    source = request_body.get('source')
    date = request_body.get('date')
    topic = request_body.get('topic')
    if not source or not date or not topic:
        raise HTTPException(status_code=400, detail='Source, date, or topic is missing')

    # Reformat date to 'year-month' for NDTV archive URL
    day, month, year = date.split('-')
    formatted_date = f'{year}-{month}'

    # NOTE: Currently, only NDTV archives are supported
    # Construct URL using formatted date and scrape NDTV archives for the specified topic
    url = f'https://archives.ndtv.com/articles/{formatted_date}.html'
    data = await ndtv_archive(url, topic, limit=3) # Limit set to 3 due to Gemini API and scraping limitations

    # document_name = f'{source}-{formatted_date}'
    # database_history(document_name, data)
    return JSONResponse(data)

@app.post('/api/url')
async def url(request: Request) -> JSONResponse:
    # Get URL value from the incoming JSON data
    request_body = await request.json()
    url = request_body.get('url')
    if not url:
        raise HTTPException(status_code=400, detail='URL is missing')

    # Scrape the URL and return as a JSON response
    data = await ndtv_url(url)
    return JSONResponse(data)

if __name__ == '__main__':
    # Start the Streamlit app in a separate process
    streamlit_process = subprocess.Popen(['streamlit', 'run', 'python-app/home.py'])

    try:
        # Start the FastAPI server
        uvicorn.run(app)
    except:
        # Ensure the Streamlit process is terminated if FastAPI server fails to start
        streamlit_process.terminate()
        streamlit_process.wait()
