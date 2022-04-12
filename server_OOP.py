import time
import threading

import requests
from flask import Flask, request, Response, session
import DataBase.create_db
# import Functionals
from datetime import datetime
app = Flask(__name__)


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


app.run()
