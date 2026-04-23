from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def insert_into_db(data, state):

    conn = sqlite3.connect("compliance.db")
    cursor = conn.cursor()

    table = "s_e_karnataka" if state == "Karnataka" else "s_e_mumbai"

    sql = f"""
    INSERT INTO {table} (
        name_of_establishment,
        type_of_establishment,
        category_of_employer,
        business_or_trade_type,
        manager,
        date_of_opening,
        work_start_time,
        work_end_time,
        intervals,
        slot1,
        slot2,
        slot3,
        slot4,
        slot5
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(sql, (
        data["name_of_establishment"],
        data["establishment_type"],
        data["category_of_employer"],
        data["business_or_trade_type"],
        data["manager"],
        data["date_of_opening"],
        data["start_time"],
        data["end_time"],
        data["interval"],
        data["slot1"],
        data["slot2"],
        data["slot3"],
        data["slot4"],
        data["slot5"]
    ))

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        establishment_type = request.form.get("establishment_type")

        mapping = {
            "Firm": "Partner",
            "AOP (Association of Persons)": "Member",
            "Company": "Director",
            "LLP (Limited Liability Partnership)": "Partner",
            "Entity owned by Central Government": "Person Appointed",
            "Entity owned by State Government": "Person Appointed",
            "Entity owned by Local Authority": "Person Appointed"
        }

        data = {
            "name_of_establishment": request.form.get("name_of_establishment"),
            "establishment_type": establishment_type,
            "category_of_employer": mapping.get(establishment_type, ""),
            "business_or_trade_type": request.form.get("business_or_trade_type"),
            "manager": request.form.get("manager"),
            "date_of_opening": request.form.get("date_of_opening"),
            "start_time": request.form.get("start_time"),
            "end_time": request.form.get("end_time"),
            "interval": request.form.get("interval"),
            "slot1": request.form.get("slot1"),
            "slot2": request.form.get("slot2"),
            "slot3": request.form.get("slot3"),
            "slot4": request.form.get("slot4"),
            "slot5": request.form.get("slot5"),
        }

        state = request.form.get("state")

        insert_into_db(data, state)

        return "Form submitted successfully bro 😤"

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)