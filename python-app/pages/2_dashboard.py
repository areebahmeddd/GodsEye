import streamlit as st

def analyse():
    st.title('Analysis Page')

    # Access the session state
    if 'analyse_url' in st.session_state:
        st.write('URL:', st.session_state.analyse_url)
    else:
        st.write('URL not found.')

analyse()
