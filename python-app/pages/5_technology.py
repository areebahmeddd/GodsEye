# Core library imports: Streamlit setup
import streamlit as st

def technology() -> None:
    print('technology.py loaded')
    # Configure Streamlit page settings
    st.set_page_config(
        page_title='Gods Eye - Overview',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Technology Overview</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    # Display the project logo and system architecture
    # st.image('assets/logo.png', use_column_width=True)
    st.markdown(
        """
        ## Project Description

        The automated news feedback system uses web crawlers to create a dataset of news articles, scrape article URLs, and optical character recognition technology to extract content from e-papers. The system is built with the Streamlit framework to generate graphs using the Plotly library for visualization on scraped data.

        Additionally, the system includes a chatbot (powered by Gemini API) that provides perspective on the latest news for users and a Chrome extension for real-time fake news detection.

        ---

        ## System Architecture

        <p align="center">
            <strong>Data Acquisition</strong>
        </p>

        **Web Scraping**: Utilizes `BeautifulSoup` library along with `httpx` library to asynchronously scrape news articles from various news sources.

        **File Scraping**: Utilizes `PyTesseract` library for image-to-text conversion and `PyMuPDF` library for PDF-to-text conversion.

        ---

        <p align="center">
            <strong>Data Analysis</strong>
        </p>

        **Gemini API**: Provides sentiment analysis, media analysis, and fake news detection services.

        **Database Storage**: Utilizes `MongoDB` database to store responses from the Gemini API.

        ---

        <p align="center">
            <strong>Data Presentation</strong>
        </p>

        **User Interface**: Utilizes the `Streamlit` framework to generate graphs using the `Plotly` library for visualization on scraped data.

        **Chrome Extension**: Provides real-time fake news detection on news articles. (Manifest V3)

        ---
        """,
        unsafe_allow_html=True
    )
    st.image('assets/architecture.png', use_column_width=True)

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

technology()
