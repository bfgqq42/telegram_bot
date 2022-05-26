import sqlite3
import os
import time


def create_db(file):
    """
    Создание файла базы данных.

    :return: нету
    """
    con = sqlite3.connect(file)
    cur = con.cursor()
    cur.execute('''CREATE TABLE stocks
                               (date text,name text, last_name text, age text, phone text)''')
    con.commit()
    con.close()


def save_data(data: list, dbname: str):
    """
    Проверка на наличие файла базы данных.
    Вписывание в базу данных.

    :return: нету
    """
    file = f'db/{dbname}.db'

    print(os.listdir('db'))

    if f'{dbname}.db' not in os.listdir('db'):
        create_db(file)

    con = sqlite3.connect(file)
    cur = con.cursor()
    cur.execute(f"INSERT INTO stocks VALUES ('{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}','{data[0]}','{data[1]}','{data[2]}','{data[3]}')")
    con.commit()
    con.close()

