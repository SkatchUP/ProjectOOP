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


def add_imt_users(id_imt, imt):
    open()
    cursor.execute('INSERT INTO imt_users(id_imt, imt) VALUES(?,?)', [id_imt, imt])
    conn.commit()

    close()


def login_id(login):
    open()
    cursor.execute('SELECT id from users WHERE login=?', [login])
    result = cursor.fetchone()
    close()
    return result


def chek_id_from_log_pas(login, password):
    open()
    cursor.execute('SELECT id from users WHERE login=? AND password=?', [login, password])
    result = cursor.fetchone()
    close()
    print(result)
    return result


def chek_imt_id(id_user):
    open()
    cursor.execute('SELECT imt from imt_users WHERE id_imt=?', [id_user])
    result = cursor.fetchone()
    close()
    return result


def change_imt(id, update_imt):
    open()
    cursor.execute('UPDATE imt_users SET imt=? WHERE id_imt=?', [update_imt, id])
    conn.commit()

    close()


create()
