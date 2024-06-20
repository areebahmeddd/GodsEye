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

    col1, col2, col3 = st.columns([2, 2, 2])

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

    row = st.columns([2, 2, 2])
    grid = [col.container(height=200) for col in row]

    with grid[0]:
        st.subheader('Article Analysis')
        if 'trending_highlight' in st.session_state:
            st.write(f'Trending :orange[Highlights]: {st.session_state.trending_highlight}')
        else:
            st.write('Trending :orange[Highlights]: Unavailable')

        if 'article_keyword' in st.session_state:
            st.write(f'Trending :violet[Keywords]: {st.session_state.article_keyword}')
        else:
            st.write('Trending :violet[Keywords]: Unavailable')

        if 'trending_organization' in st.session_state:
            st.write(f'Trending :blue[Organizations]: {st.session_state.trending_organization}')
        else:
            st.write('Trending :blue[Organizations]: Unavailable')

    with grid[1]:
        st.subheader('Sentiment Analysis')
        if 'average_positivity' in st.session_state:
            st.write(f'Average :green[Positivity]: {st.session_state.average_positivity}')
        else:
            st.write('Average :green[Positivity]: Unavailable')

        if 'average_neutrality' in st.session_state:
            st.write(f'Average :grey[Neutrality]: {st.session_state.average_neutrality}')
        else:
            st.write('Average :grey[Neutrality]: Unavailable')

        if 'average_negativity' in st.session_state:
            st.write(f'Average :red[Negativity]: {st.session_state.average_negativity}')
        else:
            st.write('Average :red[Negativity]: Unavailable')

    with grid[2]:
        st.subheader('Media Analysis')
        if 'total_article' in st.session_state:
            st.write(f':orange[Total] Articles: {st.session_state.total_article}')
        else:
            st.write(':orange[Total] Articles: Unavailable')

        if 'flagged_article' in st.session_state:
            st.write(f':red[Flagged] Articles: {st.session_state.flagged_article}')
        else:
            st.write(':red[Flagged] Articles: Unavailable')

        if 'ai_content' in st.session_state:
            st.write(f':green[AI Generated] Content: {st.session_state.ai_content}')
        else:
            st.write(':green[AI Generated] Content: Unavailable')

    st.divider()

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

search()
