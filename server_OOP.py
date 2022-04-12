import time
import threading

import requests
from flask import Flask, request, Response, session
import DataBase.create_db
# import Functionals
from datetime import datetime
app = Flask(__name__)
global_login = ''


@app.route('/')
def start():
    return 'Working...'


@app.route('/registration', methods=['POST'])
def register():
    login = request.json['login']
    password = request.json['password']
    chek_password = request.json['return_password']
    if password == chek_password:
        DataBase.create_db.add_users(login, password)
        return Response(status=200)
    elif login == '' or password == '' or chek_password == '':
        return Response(status=400)
    else:
        return Response(status=401)


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    global global_login
    if request.method == 'POST':
        login = request.json['login']
        global_login = login
        password = request.json['password']
        id_user = DataBase.create_db.chek_log_pas_id(login, password)
        if id_user:
            db_login = DataBase.create_db.login_id(login)
            return Response(status=200)
        else:
            return Response(status=201)
    else:
        db_login = DataBase.create_db.login_id(global_login)
        return {'id_login': db_login}
    

app.run()
