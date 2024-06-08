import streamlit as st
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

    with open('news_config.json') as file:
        news_data = json.load(file)

    col1, col2, col3 = st.columns([4, 2, 4])

    with col1:
        st.session_state.news_source = st.selectbox('News Source', news_data['news_sources'], index=None)

    with col2:
        st.session_state.news_date = st.date_input('News Date', datetime.now(), format='DD/MM/YYYY')

    with col3:
        st.session_state.news_topic = st.selectbox('News Topic', news_data['news_topics'], index=None)

    if st.button('Search', use_container_width=True):
        if not st.session_state.news_source or not st.session_state.news_topic:
            st.warning('Please select the news source and topic', icon=':material/warning:')
        else:
            st.switch_page('pages/1_search.py')

    st.markdown(
        "<p style='text-align: center;'>───── Or ─────</p>",
        unsafe_allow_html=True
    )

    st.session_state.article_url = st.text_input('Article URL')

    if st.button('Analyse', use_container_width=True):
        if not st.session_state.article_url:
            st.warning('Please enter the article URL', icon=':material/warning:')
        else:
            st.switch_page('pages/2_analyse.py')

    st.markdown(
        "<h1 style='text-align: center;'>Project Demo</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    st.video('https://www.youtube.com/watch?v=D0D4Pa22iG0')

    st.markdown(
        "<h1 style='text-align: center;'>Team</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    row1, row2 = st.columns(2), st.columns(2)
    grid = [col.container(height=560) for col in row1 + row2]

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
            'Hemamalini',
            'assets/hemamalini.png',
            'Backend Developer',
            '1ds22cb091@dsce.edu.in',
            'https://github.com/1DS22CS091hemamalini',
            'https://linkedin.com/in/hemamalini-srinivas-191a96256'
        )

    with grid[2]:
        person_card(
            'Shivansh',
            'assets/shivansh.png',
            'Chrome Extension Developer',
            'shivansh.karan@gmail.com',
            'https://github.com/SpaceTesla',
            'https://linkedin.com/in/shivansh-karan'
        )

    with grid[3]:
        person_card(
            'Anish',
            'assets/anish.png',
            'App Developer',
            'anishvarma.ava@gmail.com',
            'https://github.com/Av7danger',
            'https://linkedin.com/in/danishvarma'
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

if __name__ == '__main__':
    index()
