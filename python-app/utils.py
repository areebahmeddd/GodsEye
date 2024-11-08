# Core library imports: Streamlit setup
import streamlit as st

# Function to apply custom CSS styles to the Streamlit app
def custom_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');

        img {
            border-radius: 0.50rem;
        }
        .ea3mdgi5 {
            padding-bottom: 96px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to create a person card component with name, image, role, email, github, and linkedin links
def person_card(name: str, image_path: str, role: str, email: str, github_link: str, linkedin_link: str) -> None:
    custom_css()
    st.image(image_path, use_column_width=True)
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <h2>{name}</h2>
            <p>{role}</p>
            <p><a href='mailto:{email}'>{email}</a></p>
            <p>
                <a href='{github_link}' target='_blank' style='text-decoration: none;'>
                    <button style='display: inline-flex; align-items: center; background-color: #24292e; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 12px;'>
                        <i class='fab fa-github' style='margin-right: 5px;'></i>
                        GitHub
                    </button>
                </a>
                <a href='{linkedin_link}' target='_blank' style='text-decoration: none;'>
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
