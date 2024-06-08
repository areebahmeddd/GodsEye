import streamlit as st

def analyse():
    st.set_page_config(page_title='Gods Eye', page_icon='assets/favicon.png', layout='wide', initial_sidebar_state='collapsed')
    st.markdown(
        "<h1 style='text-align: center;'>Dashboard</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

    with col1:
        if 'article_url' in st.session_state:
            col1 = st.text_input('Published By', value=st.session_state.article_url)
        else:
            col1 = st.text_input('Published By', value='Unavailable')

    with col2:
        if 'published_date' in st.session_state:
                col2 = st.text_input('Published Date', value=st.session_state.published_date)
        else:
            col2 = st.text_input('Published Date', value='Unavailable')

    with col3:
        if 'author' in st.session_state:
            col3 = st.text_input('Written By', value=st.session_state.author)
        else:
            col3 = st.text_input('Written By', value='Unavailable')

    with col4:
        if 'edited_date' in st.session_state:
            col4 = st.text_input('Last Edited', value=st.session_state.edited_date)
        else:
            col4 = st.text_input('Last Edited', value='Unavailable')

    if 'article_summary' in st.session_state:
        st.text_area('Article Summary', value=st.session_state.article_summary, height=100, help='Powered by Gemini')
    else:
        st.text_area('Article Summary', value='Unavailable', height=100, help='Powered by Gemini')

    if 'article_authenticity' in st.session_state:
        st.text_area('Verification & Credibility Check', value=st.session_state.article_authenticity, height=200, help='Powered by Gemini')
    else:
        st.text_area('Verification & Credibility Check', value='Unavailable', height=100, help='Powered by Gemini')

    st.divider()

    row = st.columns([2, 2, 2])
    grid = [col.container(height=200) for col in row]

    with grid[0]:
        st.subheader('Article Analysis')
        if 'article_highlight' in st.session_state:
            st.write(f':orange[Highlight]: {st.session_state.article_highlight}')
        else:
            st.write(':orange[Highlight]: Unavailable')

        if 'article_organization' in st.session_state:
            st.write(f':blue[Organization]: {st.session_state.article_organization}')
        else:
            st.write(':blue[Organization]: Unavailable')

    with grid[1]:
        st.subheader('Sentiment Analysis')
        if 'article_positivity' in st.session_state:
            st.write(f':green[Positive]: {st.session_state.article_positivity}')
        else:
            st.write(':green[Positive]: Unavailable')

        if 'article_neutrality' in st.session_state:
            st.write(f':grey[Neutral]: {st.session_state.article_neutrality}')
        else:
            st.write(':grey[Neutral]: Unavailable')

        if 'article_negativity' in st.session_state:
            st.write(f':red[Negative]: {st.session_state.article_negativity}')
        else:
            st.write(':red[Negative]: Unavailable')

    with grid[2]:
        st.subheader('Media Analysis')
        if 'article_language' in st.session_state:
            st.write(f':green[Language]: {st.session_state.article_language}')
        else:
            st.write(':green[Language]: Unavailable')

        if 'read_time' in st.session_state:
            st.write(f':red[Read Time]: {st.session_state.read_time}')
        else:
            st.write(':red[Read Time]: Unavailable')

        if 'article_links' in st.session_state:
            st.write(f':violet[Links]: {st.session_state.article_links}')
        else:
            st.write(':violet[Links]: Unavailable')

        if 'article_images' in st.session_state:
            st.write(f':orange[Images]: {st.session_state.article_images}')
        else:
            st.write(':orange[Images]: Unavailable')

        if 'article_videos' in st.session_state:
            st.write(f':blue[Videos]: {st.session_state.article_videos}')
        else:
            st.write(':blue[Videos]: Unavailable')

    st.divider()

analyse()
