# Core library imports: Streamlit setup
import streamlit as st
# Local project-specific imports: chat session with Gemini API
from gemini import chat_session

def chat() -> None:
    # Configure Streamlit page settings
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

    # Initialize empty list to store chat messages in session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages with roles and content fetched from session state
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # Store user input in session state as a message with the role 'user'
    if prompt := st.chat_input('Ready for a new perspective?'):
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        # Send user input to Gemini API and display the response as a message with the role 'assistant'
        with st.spinner('Creating a new perspective...'):
            response = chat_session.send_message(prompt)
            if response.candidates:
                assistant_response = response.candidates[0].content.parts[0].text
            else:
                assistant_response = "I'm sorry, but I couldn't generate a response."

        # Display the assistant response in the chat
        with st.chat_message('assistant'):
            st.markdown(assistant_response)
        # Store the assistant response in session state as a message with the role 'assistant'
        st.session_state.messages.append({'role': 'assistant', 'content': assistant_response})

chat()
