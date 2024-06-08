import streamlit as st

def feedback():
    st.set_page_config(
        page_title='Gods Eye - Feedback',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Contact Us</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    with st.form('contact_form'):
        st.subheader("📬Let's get in touch!")

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input('Name')

        with col2:
            email = st.text_input('Email')

        message = st.text_area('Message', height=200, help='End-to-end encrypted.')

        if st.form_submit_button('Submit', use_container_width=True):
            if not name or not email or not message:
                st.warning('Please fill in all the fields', icon=':material/warning:')
            else:
                st.success("Thank you! We've received your message and will get back to you soon :)", icon=':material/check_circle:')

feedback()
