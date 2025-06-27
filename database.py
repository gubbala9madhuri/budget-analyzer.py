import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        note TEXT,
        date TEXT
    )''')
    conn.commit()
    conn.close()

def add_expense(amount, category, note, date):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
              (amount, category, note, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT amount, category, note, date FROM expenses")
    data = c.fetchall()
    conn.close()
    return data