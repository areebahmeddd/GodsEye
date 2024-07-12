# Core library imports: Streamlit setup
import streamlit as st

def scan() -> None:
    print('scan.py loaded')
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

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

# Check if the article pdf is in session state to prevent direct URL access to this page
if 'article_pdf' in st.session_state:
    scan()
else:
    st.switch_page('home.py')
