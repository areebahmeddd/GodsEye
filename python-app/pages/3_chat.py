import streamlit as st

def chat():
    st.set_page_config(
        page_title='Gods Eye - Chat',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Perspec AI</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt := st.chat_input('Ready for a new perspective?'):
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        with st.chat_message('assistant'):
            st.markdown(prompt)
        st.session_state.messages.append({'role': 'assistant', 'content': prompt})

chat()
