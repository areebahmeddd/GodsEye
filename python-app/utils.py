import streamlit as st

def custom_css():
    st.markdown(
        """
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');

        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .btn {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #5588ff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            width: 100%;
        }
        .btn i {
            margin-right: 8px;
        }
        .btn:hover {
            background-color: #3366ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def create_button(icon, label):
    return f"""<button class="btn"><i class="fas fa-{icon}"></i>{label}</button>"""
