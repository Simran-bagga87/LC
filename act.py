import streamlit as st
from datetime import time

st.image("compliance.jpg", use_container_width=True)
st.title("Name of the Act for Compliance")
# 🧊 APPLY CARD STYLE TO STREAMLIT CONTAINER
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/004/394/388/small/abstract-dark-blue-fluid-wave-background-free-vector.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

/* -------- Container Alignment -------- */
.stTextInput,
.stNumberInput,
.stDateInput,
.stSelectbox,
.stPasswordInput {
    
    margin: 12px auto;
}

/* -------- Input Fields -------- */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stPasswordInput input {

    background-color: #000 !important;
    color: white !important;

    border: 1px solid #1f2937 !important;
    border-radius: 8px;
    padding: 10px;

    transition: all 0.25s ease;
}

/* -------- Selectbox CLOSED -------- */
div[data-baseweb="select"] > div {

    background-color: #000 !important;
    color: white !important;

    border: 1px solid #1f2937 !important;
    border-radius: 8px;

    transition: all 0.25s ease;
}

/* -------- Hover Effect -------- */
.stTextInput input:hover,
.stNumberInput input:hover,
.stDateInput input:hover,
.stPasswordInput input:hover,
div[data-baseweb="select"] > div:hover {

    border-color: #0a84ff !important;
    box-shadow: 0 0 8px rgba(10,132,255,0.5);
}

/* -------- Focus Effect -------- */
.stTextInput input:focus,
.stNumberInput input:focus,
.stDateInput input:focus,
.stPasswordInput input:focus,
div[data-baseweb="select"]:focus-within > div {

    border-color: #0a84ff !important;
    box-shadow: 0 0 12px rgba(10,132,255,0.8);
    outline: none !important;
}

/* -------- Dropdown Menu (OPENED OPTIONS) -------- */
ul[role="listbox"] {
    background-color: #000 !important;
    color: white !important;
    border: 1px solid #1f2937 !important;
}

/* -------- Dropdown Options -------- */
li[role="option"] {
    background-color: #000 !important;
    color: white !important;
}

/* -------- Option Hover -------- */
li[role="option"]:hover {
    background-color: #0a84ff !important;
    color: white !important;
}

/* -------- Placeholder -------- */
input::placeholder {
    color: #9ca3af;
}
    </style>
    """,
    unsafe_allow_html=True
)



if "page" not in st.session_state:
    st.session_state.page = 1


st.text_input("Enter the Act Name")
    

if st.button("Next"):
    from labour_compliance import establishment
    establishment()