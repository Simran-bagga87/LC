import streamlit as st
from datetime import time
import pandas as pd

import os
from supabase import create_client

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

## Transform 
def transform(data):
    return (
        data["Name of Establishment"],
        data["Type of Establishment"],
        data["Category of Employer"],
        data["Business or Trade Type"],
        data["Manager"],
        data["Date of Opening of Business"],
        data["Work Start Time"].strftime("%H:%M"),
        data["Work End Time"].strftime("%H:%M"),
        data["Intervals"],
        data["Slot 1"],
        data["Slot 2"],
        data["Slot 3"],
        data["Slot 4"],
        data["Slot 5"]
    )

def insert_into_db(data, state):


        table = "s_e_karnataka" if state == "Karnataka" else "s_e_mumbai"

        supabase.table(table).insert({
        "name_of_establishment": data["Name of Establishment"],
        "type_of_establishment": data["Type of Establishment"],
        "category_of_employer": data["Category of Employer"],
        "business_or_trade_type": data["Business or Trade Type"],
        "manager": data["Manager"],
        "date_of_opening": str(data["Date of Opening of Business"]),
        "work_start_time": data["Work Start Time"].strftime("%H:%M"),
        "work_end_time": data["Work End Time"].strftime("%H:%M"),
        "intervals": data["Intervals"],
        "slot1": data["Slot 1"],
        "slot2": data["Slot 2"],
        "slot3": data["Slot 3"],
        "slot4": data["Slot 4"],
        "slot5": data["Slot 5"],
    }).execute()

# establishment form
def shop_e_establishment():
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
    return name_of_establishment,establishment_type,category_of_employer,business_or_trade_type,manager,date_of_opening,start_time,end_time,interval,slots





# main
st.image("compliance.jpg", use_container_width=True)
st.title("Labour Compliance Form")

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

st.header("ACT")
name_of_act = st.selectbox("Name of the Act for Compliance",["test","Shops and Establishments Act 2017"])

if name_of_act=="Shops and Establishments Act 2017":
    state = st.selectbox("State for the Compliance",["Karnataka","Mumbai"])
    name_of_establishment,establishment_type,category_of_employer,business_or_trade_type,manager,date_of_opening,start_time,end_time,interval,slots = shop_e_establishment()


    slot1,slot2,slot3,slot4,slot5 = slots
    if st.button("Submit"):
        df = {
    "Name of Establishment": name_of_establishment,
    "Type of Establishment": establishment_type,
    "Category of Employer": category_of_employer,
    "Business or Trade Type":business_or_trade_type,
    "Manager": manager,
    "Date of Opening of Business": date_of_opening,
    "Work Start Time": start_time,
    "Work End Time": end_time,
    "Intervals": interval,
    "Slot 1": slot1,
    "Slot 2": slot2,
    "Slot 3": slot3,
    "Slot 4": slot4,
    "Slot 5":slot5
    }


# ----------------------------
# INSERT FUNCTION
# ----------------------------
    

            

        insert_into_db(df, state)
        st.write("form submitted")




