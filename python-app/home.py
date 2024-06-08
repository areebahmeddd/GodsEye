import streamlit as st
import json
from datetime import datetime
from utils import custom_css

def index():
    st.set_page_config(page_title='Gods Eye', page_icon='assets/favicon.png', layout='centered', initial_sidebar_state='collapsed')
    st.markdown(
        "<h1 style='text-align: center;'>Gods Eye: Automated Feedback System</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    with open('news_config.json') as file:
        news_data = json.load(file)

    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        st.session_state.news_source = st.selectbox('News Source', news_data['news_sources'])

    with col2:
        st.session_state.news_date = st.date_input('News Date', datetime.now())

    with col3:
        st.session_state.news_topic = st.selectbox('News Topic', news_data['news_topics'])

    if st.button('Search', use_container_width=True):
        st.switch_page('pages/1_dashboard.py')

    st.markdown(
        "<p style='text-align: center;'>───── Or ─────</p>",
        unsafe_allow_html=True
    )

    st.session_state.article_url = st.text_input('Article URL')

    if st.button('Analyse', use_container_width=True):
        st.switch_page('pages/2_dashboard.py')

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
    grid = [col.container(height=500) for col in row1 + row2]
    custom_css()

    with grid[0]:
        st.image('assets/areeb.png', use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <h2>Areeb</h2>
                <p><a href='mailto:areebshariff@acm.org'>areebshariff@acm.org</a></p>
                <p>
                    <a href='https://github.com/areebahmeddd' target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #24292e; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 12px;'>
                            <i class='fab fa-github' style='margin-right: 5px;'></i>
                            GitHub
                        </button>
                    </a>
                    <a href='https://linkedin.com/in/areebahmeddd' target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #0077b5; color: white; border: none; padding: 5px 10px; cursor: pointer; margin-left: 10px; border-radius: 12px;'>
                            <i class='fab fa-linkedin' style='margin-right: 5px;'></i>
                            LinkedIn
                        </button>
                    </a>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with grid[1]:
        st.image('https://avatars.githubusercontent.com/u/66689009?v=4', use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <h2>Shivansh</h2>
                <p><a href='mailto:shivansh.karan@gmail.com'>shivansh.karan@gmail.com</a></p>
                <p>
                    <a href='https://github.com/SpaceTesla' target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #24292e; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 12px;'>
                            <i class='fab fa-github' style='margin-right: 5px;'></i>
                            GitHub
                        </button>
                    </a>
                    <a href='https://linkedin.com/in/shivansh-karan' target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #0077b5; color: white; border: none; padding: 5px 10px; cursor: pointer; margin-left: 10px; border-radius: 12px;'>
                            <i class='fab fa-linkedin' style='margin-right: 5px;'></i>
                            LinkedIn
                        </button>
                    </a>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with grid[2]:
        st.image('https://avatars.githubusercontent.com/u/66689009?v=4', use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <h2>Hemamalini</h2>
                <p><a href='mailto:1ds22cb091@dsce.edu.in'>1ds22cb091@dsce.edu.in</a></p>
                <p>
                    <a href='https://github.com/1DS22CS091hemamalini' target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #24292e; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 12px;'>
                            <i class='fab fa-github' style='margin-right: 5px;'></i>
                            GitHub
                        </button>
                    </a>
                    <a href='https://linkedin.com/in/hemamalini-srinivas-191a96256' target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #0077b5; color: white; border: none; padding: 5px 10px; cursor: pointer; margin-left: 10px; border-radius: 12px;'>
                            <i class='fab fa-linkedin' style='margin-right: 5px;'></i>
                            LinkedIn
                        </button>
                    </a>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with grid[3]:
        st.image('https://avatars.githubusercontent.com/u/66689009?v=4', use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <h2>Anish</h2>
                <p><a href='mailto:anishvarma.ava@gmail.com'>anishvarma.ava@gmail.com</a></p>
                <p>
                    <a href="https://github.com/Av7danger" target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #24292e; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 12px;'>
                            <i class='fab fa-github' style='margin-right: 5px;'></i>
                            GitHub
                        </button>
                    </a>
                    <a href="https://linkedin.com/in/danishvarma" target='_blank' style='text-decoration: none;'>
                        <button style='display: inline-flex; align-items: center; background-color: #0077b5; color: white; border: none; padding: 5px 10px; cursor: pointer; margin-left: 10px; border-radius: 12px;'>
                            <i class='fab fa-linkedin' style='margin-right: 5px;'></i>
                            LinkedIn
                        </button>
                    </a>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 20px;'>
            <p>Powered by Gemini</p>
            <a href="https://github.com/areebahmeddd/GodsEye/blob/main/LICENSE">License</a> •
            <a href="https://github.com/areebahmeddd/GodsEye/blob/main/README.md">Documentation</a>
        </footer>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    index()
