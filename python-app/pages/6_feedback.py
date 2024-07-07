# Core library imports: Streamlit setup and email functionality
import smtplib
import streamlit as st

from config import ADMIN_EMAIL, ADMIN_PASSWORD

def feedback() -> None:
    # Configure Streamlit page settings
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

    # Create a form for users to submit feedback
    with st.form('contact_form'):
        st.subheader("📬Let's get in touch!")

        # Create 2-column layout
        col1, col2 = st.columns(2)

        # Create text input fields for name and email
        with col1:
            name = st.text_input('Name')

        with col2:
            email = st.text_input('Email')

        # Create a text area for the message and a submit button
        message = st.text_area('Message', height=200, help='End-to-end encrypted')
        if st.form_submit_button('Submit', use_container_width=True):
            if not name or not email or not message:
                st.warning('Please fill in all the fields', icon=':material/warning:')
            else:
                result = send_mail(name, email, message)
                if 'successfully' in result:
                    st.success("Thank you! We've received your message and will get back to you soon :)", icon=':material/check_circle:')
                else:
                    st.error('Error occurred while sending the email', icon=':material/error:')

    st.markdown(
        """
        <footer style='text-align: center; margin-top: 40px;'>
            <p>Powered by Gemini</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def send_mail(name, email, message) -> str:
    # Load admin email and password from Streamlit secrets.toml
    # ADMIN_EMAIL = st.secrets["admin"]["email"]
    # ADMIN_PASSWORD = st.secrets["admin"]["app_pass"]

    # Construct the email subject and body
    subject = 'GodsEye Feedback Team'
    body = f'Hey {name}, Thank you for your feedback!\n\nHere is a copy of your message:\n\n{message}'
    full_message = f'Subject: {subject}\n\n{body}'

    try:
        # Send the email using the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user=ADMIN_EMAIL, password=ADMIN_PASSWORD)
        server.sendmail(from_addr=ADMIN_EMAIL, to_addrs=email, msg=full_message)
        server.sendmail(from_addr=ADMIN_EMAIL, to_addrs='areebahmed0709@gmail.com', msg=full_message)
        server.quit()
        return 'Email sent successfully'

    except Exception as exc:
        return str(exc)

feedback()
