import streamlit as st
import requests
import json
from datetime import datetime

from utils import custom_css, person_card

def index():
    st.set_page_config(
        page_title='Gods Eye',
        page_icon='assets/favicon.png',
        layout='centered',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Gods Eye: Automated Feedback System</h1>",
        unsafe_allow_html=True
    )
    st.divider()
    st.info('NOTE: The application is currently in alpha phase. Some features are limited and undergoing development.', icon=':material/info:')

    with open('news_config.json') as file:
        news_data = json.load(file)

    col1, col2, col3 = st.columns([4, 2, 4])

    with col1:
        st.session_state.news_source = st.selectbox('News Source', news_data['news_sources'], index=None)

    with col2:
        st.session_state.news_date = st.date_input('News Date', datetime.now(), format='DD-MM-YYYY')

    with col3:
        st.session_state.news_topic = st.selectbox('News Topic', news_data['news_topics'], index=None)

    if st.button('Search', use_container_width=True):
        if not st.session_state.news_source or not st.session_state.news_topic:
            st.warning('Please select the news source and topic', icon=':material/warning:')
        else:
            api_response = requests.post(
                'http://localhost:8000/api/archive',
                json={
                    'source': st.session_state.news_source,
                    'date': st.session_state.news_date.strftime('%d-%m-%Y'),
                    'topic': st.session_state.news_topic
                }
            )
            if api_response.status_code == 200:
                st.session_state.search_results = api_response.json()
                st.switch_page('pages/1_search.py')
            else:
                st.error('Error occurred while processing the news articles', icon=':material/error:')

    st.markdown(
        "<p style='text-align: center;'>───── Or ─────</p>",
        unsafe_allow_html=True
    )

    st.session_state.article_url = st.text_input('Article URL')

    if st.button('Analyse', use_container_width=True):
        if not st.session_state.article_url:
            st.warning('Please enter the article URL', icon=':material/warning:')
        else:
            api_response = requests.post(
                'http://localhost:8000/api/url',
                json={'url': st.session_state.article_url}
            )
            if api_response.status_code == 200:
                st.session_state.update(api_response.json())
                st.switch_page('pages/2_analyse.py')
            else:
                st.error('Error occurred while processing the article', icon=':material/error:')

    st.markdown(
        "<h1 style='text-align: center;'>Project Demo</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    st.video('https://youtube.com/watch?v=GFApJyF8yc0')

    st.markdown(
        "<h1 style='text-align: center;'>Team</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    row = st.columns(2)
    grid = [col.container(height=560) for col in row]

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

index()
