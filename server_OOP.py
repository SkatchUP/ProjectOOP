import time
import threading

import requests
from flask import Flask, request, Response, redirect, render_template, session
from datetime import datetime
app = Flask(__name__)

users = []

@app.route('/')
def start():
    return 'Working...'


@app.route('/registration', methods=['POST'])
def register():
    login = request.json['login']
    password = request.json['password']
    return_password = request.json['return_password']
    full_info = {'login': login, 'password': password, 'return_password': return_password}
    if full_info['login'] == '' or full_info['password'] == '' or full_info['return_password'] == '':
        return Response(status=400)
    else:
        users.append(full_info)
        print(full_info)
        print(users)
        return Response(status=200)

app.run()