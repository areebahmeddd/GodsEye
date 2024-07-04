<p align="center">
  <img src="https://github.com/areebahmeddd/GodsEye/blob/main/assets/logo.png" alt="Project Logo">
</p>

## Project Description

The automated feedback system uses web crawlers to create a dataset of news articles, scrape article URLs, and optical character recognition technology to extract content from e-papers. The system is built with the Streamlit framework to generate graphs using the Plotly library for visualization of scraped data.

Additionally, the system includes a chatbot (powered by the Gemini API) that provides perspective on the latest news for users and a Chrome extension for real-time fake news detection.

## System Architecture

<p align="center">
  <strong>Data Acquisition</strong>
</p>

**Web Scraping**: Utilizes the `BeautifulSoup` library along with the `httpx` library to asynchronously scrape news articles from various news sources.

**File Scraping**: Utilizes the `PyTesseract` library for image-to-text conversion and the `PyMuPDF` library for PDF-to-text conversion.

---

<p align="center">
  <strong>Data Analysis</strong>
</p>

**Gemini API**: Provides sentiment analysis, media analysis, and fake news detection services.

**Database Storage**: Utilizes the `MongoDB` database to store responses from the Gemini API.

---

<p align="center">
  <strong>Data Presentation</strong>
</p>

**User Interface**: Utilizes the `Streamlit` framework to generate graphs using the `Plotly` library for visualization of scraped data.

**Chrome Extension**: Provides real-time fake news detection on news articles (Manifest V3).

---

<p align="center">
  <img src="https://github.com/areebahmeddd/GodsEye/blob/main/assets/architecture.png" alt="System Architecture">
</p>

## Getting Started

Follow these steps to set up and run the GodsEye software on your local machine, or you can watch the [demo video](https://youtube.com/watch?v=GFApJyF8yc0).

## Installation

1. Clone the repository to your local machine:
    ```shell
    git clone https://github.com/areebahmeddd/GodsEye.git
    ```

2. Navigate to the project directory:
    ```shell
    cd GodsEye
    ```

3. Create a virtual environment (optional but recommended):
    ```shell
    python -m venv .venv
    ```

4. Activate the virtual environment:
    - Windows:
        ```shell
        .venv\Scripts\activate
        ```
    - macOS and Linux:
        ```shell
        source .venv/bin/activate
        ```

5. Install the project dependencies:
    ```shell
    pip install -r requirements.txt
    ```

6. Set up the Chrome extension:
    - Open Chrome and go to `chrome://extensions`.
    - Enable "Developer mode" (top right corner).
    - Click "Load unpacked".
    - Select the `browser-extension` folder in the GodsEye repository.

## Usage

1. Run the application and start the development server:
    ```shell
    python python-app/app.py
    ```
    ```shell
    streamlit run python-app/home.py
    ```

## License

This project is licensed under the [Apache License 2.0](https://github.com/areebahmeddd/GodsEye/blob/main/LICENSE).

## Authors

[Areeb Ahmed](https://github.com/areebahmeddd) and [Shivansh Karan](https://github.com/SpaceTesla)
