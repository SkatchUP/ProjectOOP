import sqlite3

from colorama import Cursor

users = 'users.sqlite'
conn, cursor = None, None


def open():
    global conn, cursor
    conn = sqlite3.connect(users)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def create():
    open()
    cursor.execute('PRAGMA foreign_key=on')
    do('''CREATE TABLE IF NOT EXISTS users(
                                            id INTEGER PRIMARY KEY,
                                            login VARCHAR,
                                            password VARCHAR)''')
    do('''CREATE TABLE IF NOT EXISTS imt_users(
                                            id_imt INTEGER PRIMARY KEY,
                                            imt VARCHAR)''')

    close()


def add_users(login, password):
    open()
    cursor.execute('INSERT INTO users(login, password) VALUES(?,?)', [login, password])
    conn.commit()

    close()


def add_imt_users(id_imt):
    open()
    cursor.execute('INSERT INTO imt_users(id_imt) VALUES(?)', [id_imt])
    conn.commit()

    close()


create()
