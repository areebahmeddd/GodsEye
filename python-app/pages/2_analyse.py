import json
import streamlit as st

def analyse():
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

    col1, col2, col3, col4 = st.columns(4)

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

    row = st.columns(3)
    grid = [col.container(height=200) for col in row]

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
        st.write(f':violet[Links]: {st.session_state.get("links", "Unavailable")}')
        st.write(f':orange[Images]: {st.session_state.get("images", "Unavailable")}')
        st.write(f':blue[Videos]: {st.session_state.get("videos", "Unavailable")}')

    st.divider()

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

required_keys = ['publisher', 'author', 'publication_date', 'edited_date']
if any(key not in st.session_state for key in required_keys):
    st.switch_page('home.py')

analyse()
