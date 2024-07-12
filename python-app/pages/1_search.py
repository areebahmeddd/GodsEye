# Core library imports: Streamlit setup
import streamlit as st
from typing import Counter

# Local project-specific imports: graph components
from graphs import *

# NOTE: session_state is a Streamlit feature that allows storing data across pages
# Reference: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
def search() -> None:
    print('search.py loaded')
    # Configure Streamlit page settings
    st.set_page_config(
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

    # Create a 3-column layout
    col1, col2, col3 = st.columns(3)

    # Display the news source, date, and topic in text inputs using session state
    with col1:
        if 'news_source' in st.session_state:
            st.text_input('News Source', value=st.session_state.news_source)
        else:
            st.text_input('News Source', value='Unavailable')

    with col2:
        if 'news_date' in st.session_state:
            st.text_input('News Date', value=st.session_state.news_date)
        else:
            st.text_input('News Date', value='Unavailable')

    with col3:
        if 'news_topic' in st.session_state:
            st.text_input('News Topic', value=st.session_state.news_topic)
        else:
            st.text_input('News Topic', value='Unavailable')

    st.divider()

    # Retrieve the search results from session state and display the first article analysis
    search_results = st.session_state.search_results
    result = search_results[0]

    # Create a 3-column layout with a grid of 200px height containers
    row = st.columns(3, gap='medium')
    grid = [col.container(height=200) for col in row]

    # Display the article analysis, sentiment analysis, and media analysis in separate containers using session state
    with grid[0]:
        st.subheader('Article Analysis')
        with st.expander('Trending Highlights'):
            st.write(result.get('trending_highlights', ['Unavailable']))

        with st.expander('Trending Keywords'):
            st.write(result.get('trending_keywords', ['Unavailable']))

        with st.expander('Trending Organizations'):
            st.write(result.get('trending_organizations', ['Unavailable']))

    with grid[1]:
        st.subheader('Sentiment Analysis')
        st.write(f'Average :green[Positivity]: {result.get("average_positive_percentage", "Unavailable")}')
        st.write(f'Average :grey[Neutrality]: {result.get("average_neutral_percentage", "Unavailable")}')
        st.write(f'Average :red[Negativity]: {result.get("average_negative_percentage", "Unavailable")}')

    with grid[2]:
        st.subheader('Media Analysis')
        st.write(f':orange[Total] Articles: {result.get("total_articles", "Unavailable")}')
        st.write(f':red[Flagged] Articles: {result.get("flagged_articles", "Unavailable")}')
        st.write(f':green[AI Generated] Content: {result.get("ai_generated_articles", "Unavailable")}')

    st.divider()

    # Create a 3-column layout with custom widths and a grid of 500px height containers
    row1, row2, row3 = st.columns(1), st.columns(1), st.columns(2)
    grid = [col.container(height=500) for col in row1 + row2 + row3]

    # Display the article analysis, sentiment analysis, and media analysis charts in separate containers
    with grid[0]:
        article_analysis_chart()

    with grid[1]:
        sentiment_analysis_dual_chart()

    with grid[2]:
        sentiment_analysis_chart()

    with grid[3]:
        media_analysis_chart()

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def article_analysis_chart() -> None:
    # Function to extract chart data from the search results
    def chart_data(key):
        # Extract the specified key from the search results and flatten the list of lists
        items = [
            item
            for article in st.session_state.search_results
            for item in article.get(key, [])
        ]

        # Count the occurrences of each item and sort them in descending order
        item_counts = dict(Counter(items))
        sorted_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)
        labels, values = zip(*sorted_items)

        return labels, values

    # Create a 2-column layout
    col1, col2 = st.columns(2)

    # Display the trending organizations and keywords as line charts using the extracted data
    with col1:
        labels, values = chart_data('trending_organizations')
        line_chart('Trending Organizations', labels, values, 'Organization', 'Mentions')

    with col2:
        labels, values = chart_data('trending_keywords')
        line_chart('Trending Keywords', labels, values, 'Keyword', 'Mentions')

def sentiment_analysis_dual_chart() -> None:
    # Duplicate the article IDs for each sentiment from the search results
    article_ids = [
        article['id']
        for article in st.session_state.search_results
        for _ in range(3)
    ]
    # Duplicate the sentiment labels for each article from the search results
    sentiments = [
        'Positive', 'Neutral', 'Negative'
    ] * len(st.session_state.search_results)
    # Extract the sentiment percentages from the search results for each sentiment
    percentages = [
        float(article.get(f'average_{sentiment}_percentage', '0%').strip('%'))
        for article in st.session_state.search_results
        for sentiment in ['positive', 'neutral', 'negative']
    ]
    # Define the colors for the stacked bar chart (Green, Grey, Red)
    colors = ['#3CB371', '#808080', '#FF6347']

    # Create a 2-column layout
    col1, col2 = st.columns(2)

    # Display the sentiment analysis by article as an area chart and stacked bar chart
    with col1:
        area_chart('Sentiment Analysis by Article', article_ids, percentages, 'Article ID', 'Percentage', sentiments, colors)

    with col2:
        stacked_bar_chart('Sentiment Analysis by Article', article_ids, percentages, 'Article ID', 'Percentage', sentiments, colors)

def sentiment_analysis_chart() -> None:
    # Define the labels for sentiment analysis categories
    labels = ['Positive', 'Neutral', 'Negative']
   # Extract the average sentiment percentages from the search results for each category
    values = [
        float(st.session_state.search_results[0].get(f'average_{sentiment.lower()}_percentage', '0%').strip('%'))
        for sentiment in labels
    ]
    # Define the colors for the pie chart (Green, Grey, Red)
    colors = ['#3CB371', '#808080', '#FF6347']
    pie_chart('Sentiment Analysis (Average)', labels, values, colors)

def media_analysis_chart() -> None:
    # Define the labels for media analysis categories
    labels = ['Total Articles', 'Flagged Articles', 'AI Generated Content']
    # Extract the counts from the search results for each category
    counts = [
        st.session_state.search_results[0].get(label.lower().replace(' ', '_'), 0)
        for label in labels
    ]
    # Define the colors for the horizontal bar chart (Orange, Red, Green)
    colors = ['#FFA500', '#FF6347', '#3CB371']
    horizontal_bar_chart('Media Analysis (Overall)', counts, labels, 'Count', 'Types', colors)

# Check if the search results is in session state to prevent direct URL access to this page
if 'search_results' in st.session_state:
    search()
else:
    st.switch_page('home.py')
