import sqlite3
import os

file = 'call-to.db'


def create_db():
    con = sqlite3.connect(file)
    cur = con.cursor()
    cur.execute('''CREATE TABLE stocks
                               (name text, last_name text, age text, phone text)''')
    con.commit()
    con.close()


def save_data(data: list):
    if file not in os.listdir(os.curdir):
        create_db()

    con = sqlite3.connect(file)
    cur = con.cursor()
    cur.execute(f"INSERT INTO stocks VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}')")
    con.commit()
    con.close()

