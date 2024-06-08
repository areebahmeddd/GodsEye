import streamlit as st
import json
from datetime import datetime
# from utils import custom_css, create_button

def index():
    st.set_page_config(page_title='Gods Eye', page_icon='👁️', layout='centered')
    st.title('Gods Eye: Automated Feedback System')

    # Initialize session state
    if 'news_data' not in st.session_state:
        with open('news_config.json') as file:
            st.session_state.news_data = json.load(file)

        st.session_state.selected_source = st.session_state.news_data['news_sources'][0]
        st.session_state.selected_date = datetime.now()
        st.session_state.selected_topic = st.session_state.news_data['news_topics'][0]

    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        selected_source = st.selectbox('News Source', st.session_state.news_data['news_sources'],
                                       index=st.session_state.news_data['news_sources'].index(st.session_state.selected_source))

    with col2:
        selected_date = st.date_input('News Date', st.session_state.selected_date)

    with col3:
        selected_topic = st.selectbox('News Topic', st.session_state.news_data['news_topics'],
                                      index=st.session_state.news_data['news_topics'].index(st.session_state.selected_topic))

    if st.button('Search', use_container_width=True):
        # Update session state
        st.session_state.selected_source = selected_source
        st.session_state.selected_date = selected_date
        st.session_state.selected_topic = selected_topic
        st.switch_page('pages/1_dashboard.py')

    st.markdown(
        """
        <p style='text-align: center;'>Or</p>
        """,
        unsafe_allow_html=True
    )

    st.session_state.analyse_url = st.text_input('Article URL')

    if st.button('Analyse', use_container_width=True):
        # Update session state
        st.session_state.analyse_url = st.session_state.analyse_url.strip()
        st.switch_page('pages/2_dashboard.py')

if __name__ == '__main__':
    index()
