# Core library imports: Streamlit setup
import json
import streamlit as st

# Local project-specific imports: graph components
from graphs import *

# NOTE: session_state is a Streamlit feature that allows storing data across pages
# Reference: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
def analyse() -> None:
    st.set_page_config(
        # Configure Streamlit page settings
        page_title='Gods Eye - Dashboard',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Dashboard</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    # Create a 4-column layout
    col1, col2, col3, col4 = st.columns(4)

    # Display the article metadata in text inputs using session state
    with col1:
        col1 = st.text_input('Published By', value=st.session_state.get('publisher', 'Unavailable'))

    with col2:
        col2 = st.text_input('Written By', value=st.session_state.get('author', 'Unavailable'))

    with col3:
        col3 = st.text_input('Published Date', value=st.session_state.get('publication_date', 'Unavailable'))

    with col4:
        col4 = st.text_input('Last Edited', value=st.session_state.get('edited_date', 'Unavailable'))

    st.text_area('Article Summary', value=st.session_state.get('content', 'Unavailable'), height=150, help='Powered by Gemini')

    authenticity = st.session_state.get('authenticity', 'Unavailable')
    st.text_area('Article Authenticity', value=json.dumps(authenticity, indent=4), height=200, help='Powered by Gemini')

    st.divider()

    # Create a 3-column layout with a grid of 200px height containers
    row = st.columns(3, gap='medium')
    grid = [col.container(height=200) for col in row]

    # Display the article analysis, sentiment analysis, and media analysis in text inputs using session state
    with grid[0]:
        st.subheader('Article Analysis')
        st.write(f':green[Category]: {st.session_state.get("category", "Unavailable")}')
        st.write(f':orange[Highlight]: {st.session_state.get("highlight", "Unavailable")}')
        st.write(f':blue[Organization]: {st.session_state.get("organization", "Unavailable")}')

    with grid[1]:
        st.subheader('Sentiment Analysis')
        st.write(f':green[Positive]: {st.session_state.get("positive_percentage", "Unavailable")}')
        with st.expander('Positive Text'):
            st.write(st.session_state.get('positive_text', 'Unavailable'))

        st.write(f':grey[Neutral]: {st.session_state.get("neutral_percentage", "Unavailable")}')
        with st.expander('Neutral Text'):
            st.write(st.session_state.get('neutral_text', 'Unavailable'))

        st.write(f':red[Negative]: {st.session_state.get("negative_percentage", "Unavailable")}')
        with st.expander('Negative Text'):
            st.write(st.session_state.get('negative_text', 'Unavailable'))

    with grid[2]:
        st.subheader('Media Analysis')
        st.write(f':green[Language]: {st.session_state.get("language", "Unavailable")}')
        st.write(f':red[Read Time]: {st.session_state.get("read_time", "Unavailable")}')
        st.write(f':violet[Ads]: {st.session_state.get("ads", "Unavailable")}')
        st.write(f':blue[Links]: {st.session_state.get("links", "Unavailable")}')
        st.write(f':orange[Images]: {st.session_state.get("images", "Unavailable")}')
        st.write(f':grey[Videos]: {st.session_state.get("videos", "Unavailable")}')
        st.write(f':green[Documents]: {st.session_state.get("documents", "Unavailable")}')

    st.divider()

    # Create a 2-column layout with a grid of 500px height containers
    row = st.columns(2)
    grid = [col.container(height=500) for col in row]

    # Display the sentiment analysis and media analysis charts using custom graph components
    with grid[0]:
        sentiment_analysis_chart()

    with grid[1]:
        media_analysis_chart()

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def sentiment_analysis_chart() -> None:
    # Define the labels for sentiment analysis categories
    labels = ['Positive', 'Neutral', 'Negative']
    # Extract the sentiment percentages from session state for each category
    values = [
        float(st.session_state.get(f'{sentiment.lower()}_percentage', '0%').strip('%'))
        for sentiment in labels
    ]
    # Define the colors for the pie chart (Green, Grey, Red)
    colors = ['#3CB371', '#808080', '#FF6347']
    pie_chart('Sentiment Analysis', labels, values, colors)

def media_analysis_chart() -> None:
    # Define the labels for media analysis categories
    labels = ['Ads', 'Links', 'Images', 'Videos', 'Documents']
    # Extract the media counts from session state for each category
    counts = [
        st.session_state.get(label.lower(), 0)
        for label in labels
    ]
    # Define the colors for the horizontal bar chart (Orange, Blue, Red, Green, Purple)
    colors = ['#FF6347', '#1E90FF', '#FFA500', '#8A2BE2', '#3CB371']
    horizontal_bar_chart('Media Analysis', counts, labels, 'Count', 'Media', colors)

# Check if the required keys are in session state to prevent direct URL access to this page
required_keys = ['publisher', 'author', 'publication_date', 'edited_date']
if all(key in st.session_state for key in required_keys):
    analyse()
else:
    st.switch_page('home.py')
