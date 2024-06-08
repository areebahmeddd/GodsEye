import streamlit as st

def search():
    st.title('Search Page')

    # Access the session state
    if 'selected_source' in st.session_state:
        st.write('News Source:', st.session_state.selected_source)
    else:
        st.write('News Source not found.')

    if 'selected_date' in st.session_state:
        st.write('News Date:', st.session_state.selected_date)
    else:
        st.write('News Date not found.')

    if 'selected_topic' in st.session_state:
        st.write('News Topic:', st.session_state.selected_topic)
    else:
        st.write('News Topic not found.')

search()
