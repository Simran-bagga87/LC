import streamlit as st
from datetime import time

def establishment():
    st.image("compliance.jpg", use_container_width=True)
    st.title("Labour Compliance Form")
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


    st.header("Establishment Details")
    name_of_establishment = st.text_input("Enter Name of Establishment")

    st.header("Work Details")

    establishment_type = st.selectbox(
        "Type of Establishment",
        [
            "Firm",
            "AOP (Association of Persons)",
            "Company",
            "LLP (Limited Liability Partnership)",
            "Entity owned by Central Government",
            "Entity owned by State Government",
            "Entity owned by Local Authority"
        ]
    )

    mapping = {
        "Firm": "Partner",
        "AOP (Association of Persons)": "Member",
        "Company": "Director",
        "LLP (Limited Liability Partnership)": "Partner",
        "Entity owned by Central Government": "Person Appointed",
        "Entity owned by State Government": "Person Appointed",
        "Entity owned by Local Authority": "Person Appointed"
    }

    category_of_employer = mapping.get(establishment_type, "")

    with st.expander("Advanced Settings"):

        business_or_trade_type = st.selectbox(
            "Business or Trade Type",
            ["Any Business Trade", "Manufacture", "Journalistic Work", "Printing Work"]
        )

        manager = st.text_input("Enter Manager Name")
        date_of_opening = st.date_input("Date of Opening of Business")

        start_time = st.time_input("Work Start Time", value=time(9, 0))
        end_time = st.time_input("Work End Time", value=time(18, 0))

        interval = st.number_input("Enter Total Intervals (Max 5)", min_value=0, max_value=5, step=1)

        break_options = [
            "No Break",
            "15 minutes",
            "30 minutes",
            "45 minutes",
            "1 hour",
            "1.5 hours"
        ]

        slots = [None] * 5

        for i in range(int(interval)):
            slots[i] = st.selectbox(
                f"Break Slot {i+1}",
                break_options,
                key=f"break_slot_{i}"
            )

