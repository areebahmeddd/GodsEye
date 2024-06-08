import streamlit as st
import json
from datetime import datetime
from utils import custom_css, create_button

def index():
    st.set_page_config(page_title='Gods Eye', page_icon='favicon.png', layout='wide')
    st.title('Gods Eye: Automated Feedback System')
    custom_css()

    with open('news_config.json') as file:
        news_data = json.load(file)

    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        selected_source = st.selectbox('News Source', news_data['news_sources'])

    with col2:
        selected_date = st.date_input('News Date', datetime.now())

    with col3:
        selected_topic = st.selectbox('News Topic', news_data['news_topics'])

    search_button = st.markdown(
        create_button('search', 'Search'),
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: center;'>Or</p>
        """, 
        unsafe_allow_html=True
    )

    st.text_input('Article URL')

    analyse_button = st.markdown(
        create_button('line-chart', 'Analyse'),
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    index()
