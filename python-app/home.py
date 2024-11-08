# Core library imports: Streamlit setup
import requests
import json
import streamlit as st
from datetime import datetime

# Local project-specific imports: custom CSS and person card components
from utils import custom_css, person_card

# NOTE: session_state is a Streamlit feature that allows storing data across pages
# Reference: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
def home() -> None:
    print('home.py loaded')
    # Configure Streamlit page settings
    st.set_page_config(
        page_title='Gods Eye',
        page_icon='assets/favicon.png',
        layout='centered',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Gods Eye: Automated News Feedback System</h1>",
        unsafe_allow_html=True
    )
    st.divider()
    st.info('NOTE: The application is currently in alpha phase. Some features are limited and undergoing development.', icon=':material/info:')

    # Load news sources and topics for the search functionality
    with open('metadata/news_config.json') as file:
        news_data = json.load(file)

    # Create a 3-column layout with custom widths
    col1, col2, col3 = st.columns([4, 2, 4])

    # Collect user inputs for news source, date, and topic using Streamlit widgets and store in session state
    with col1:
        st.session_state.news_source = st.selectbox('News Source', news_data['news_sources'], index=None)

    with col2:
        st.session_state.news_date = st.date_input('News Date', datetime.now(), format='DD-MM-YYYY')

    with col3:
        st.session_state.news_topic = st.selectbox('News Topic', news_data['news_topics'], index=None)

    # Create a search button to trigger the API request and display the search results
    if st.button('Search', use_container_width=True):
        if not st.session_state.news_source or not st.session_state.news_topic:
            st.warning('Please select the news source and topic', icon=':material/warning:')
        else:
            st.warning('Please wait up to 30 seconds for the results to load', icon=':material/info:')
            # Send a POST request to the FastAPI backend with the selected source, date, and topic
            api_response = requests.post(
                'http://localhost:8000/api/archive',
                json={
                    'source': st.session_state.news_source,
                    'date': st.session_state.news_date.strftime('%d-%m-%Y'),
                    'topic': st.session_state.news_topic
                }
            )
            if api_response.status_code == 200:
                # Store the search results in session state and switch to the search results page
                st.session_state.search_results = api_response.json()
                st.switch_page('pages/1_search.py')
            else:
                st.error('Error occurred while processing the news articles', icon=':material/error:')

    st.markdown(
        "<p style='text-align: center;'>───── Or ─────</p>",
        unsafe_allow_html=True
    )

    # Create a text input for the article URL and a button to trigger the API request
    st.session_state.article_url = st.text_input('Article URL')
    if st.button('Analyse', use_container_width=True):
        if not st.session_state.article_url:
            st.warning('Please enter the article URL', icon=':material/warning:')
        else:
            st.warning('Please wait up to 30 seconds for the results to load', icon=':material/info:')
            # Send a POST request to the FastAPI backend with the article URL
            api_response = requests.post(
                'http://localhost:8000/api/url',
                json={'url': st.session_state.article_url}
            )
            if api_response.status_code == 200:
                # Store the analysis results in session state and switch to the analysis page
                st.session_state.update(api_response.json())
                st.switch_page('pages/2_analyse.py')
            else:
                st.error('Error occurred while processing the news article', icon=':material/error:')

    st.markdown(
        "<p style='text-align: center;'>───── Or ─────</p>",
        unsafe_allow_html=True
    )

    # Create a file uploader for the article PDF and a button to trigger the API request
    st.session_state.article_pdf = st.file_uploader('Article PDF')
    if st.button('Scan', use_container_width=True):
        st.warning('This feature is currently under development', icon=':material/warning:')
        # if not st.session_state.article_pdf:
        #     st.warning('Please upload the article PDF', icon=':material/warning:')
        # else:
        #     st.warning('Please wait up to 30 seconds for the results to load', icon=':material/info:')
        #     # Send a POST request to the FastAPI backend with the article PDF
        #     api_response = requests.post(
        #         'http://localhost:8000/api/pdf',
        #         files={'pdf': st.session_state.article_pdf}
        #     )
        #     if api_response.status_code == 200:
        #         # Store the scan results in session state and switch to the scan page
        #         st.session_state.update(api_response.json())
        #         st.switch_page('pages/3_scan.py')
        #     else:
        #         st.error('Error occurred while processing the news pdf', icon=':material/error:')

    st.markdown(
        "<h1 style='text-align: center;'>Project Demo</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    st.video('https://youtube.com/watch?v=sWd4kOQU9as')

    st.markdown(
        "<h1 style='text-align: center;'>Team</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    # Create a 2-column layout with a grid of 580px height containers
    row = st.columns(2)
    grid = [col.container(height=580) for col in row]

    # Display the team members information using the custom person card component
    with grid[0]:
        person_card(
            'Areeb',
            'assets/areeb.png',
            'Full-Stack Developer',
            'areebshariff@acm.org',
            'https://github.com/areebahmeddd',
            'https://linkedin.com/in/areebahmeddd'
        )

    with grid[1]:
        person_card(
            'Shivansh',
            'assets/shivansh.png',
            'Chrome Extension Developer',
            'shivansh.karan@gmail.com',
            'https://github.com/SpaceTesla',
            'https://linkedin.com/in/shivansh-karan'
        )

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
            <a href="https://github.com/areebahmeddd/GodsEye/blob/main/LICENSE">License</a> •
            <a href="https://github.com/areebahmeddd/GodsEye/blob/main/README.md">Documentation</a>
        </footer>
        """,
        unsafe_allow_html=True
    )

home()
