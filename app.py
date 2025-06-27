import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
from database import init_db, add_expense, get_expenses

init_db()
st.title("💰 Budget Analyzer with Weekly Summary")


st.subheader("Add New Expense")
amount = st.number_input("Amount", min_value=0.0)
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
note = st.text_input("Note (optional)")
expense_date = st.date_input("Date", value=date.today())

if st.button("Add Expense"):
    add_expense(amount, category, note, str(expense_date))
    st.success("Expense added!")

st.subheader("📊 Weekly Summary")

data = get_expenses()
df = pd.DataFrame(data, columns=["Amount", "Category", "Note", "Date"])
df["Date"] = pd.to_datetime(df["Date"])
week_ago = datetime.now() - timedelta(days=7)
weekly_df = df[df["Date"] >= week_ago]

st.write("Total spent this week:", weekly_df["Amount"].sum())
st.write("Average per day:", weekly_df["Amount"].sum() / 7)


fig1, ax1 = plt.subplots()
weekly_df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%", ax=ax1)
ax1.set_ylabel("")
ax1.set_title("Spending by Category")
st.pyplot(fig1)


fig2, ax2 = plt.subplots()
weekly_df.groupby(weekly_df["Date"].dt.date)["Amount"].sum().plot(kind="bar", ax=ax2)
ax2.set_title("Daily Spending")
ax2.set_ylabel("Amount")
st.pyplot(fig2)