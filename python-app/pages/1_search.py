import streamlit as st

def search():
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

    col1, col2, col3 = st.columns(3)

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

    if 'search_results' in st.session_state:
        search_results = st.session_state.search_results
        result = search_results[0]

        row = st.columns(3, gap='medium')
        grid = [col.container(height=200) for col in row]

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
    else:
        st.write('No search results available')

    st.divider()

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

if 'search_results' in st.session_state:
    search()
else:
    st.switch_page('home.py')
