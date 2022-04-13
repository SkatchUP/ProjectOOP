from flask import Flask, request, Response
import DataBase.create_db
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
        id_user = DataBase.create_db.chek_id_from_log_pas(login, password)
        if id_user:
            imt_id_user = DataBase.create_db.chek_imt_id(id_user[0])
            if imt_id_user:
                return Response(status=300)
            else:
                return Response(status=200)
        else:
            return Response(status=201)
    else:
        db_login = DataBase.create_db.login_id(global_login)
        return {'id_login': db_login}


@app.route('/imt', methods=['POST', 'GET'])
def add_imt():
    if request.method == 'POST':
        id_imt = request.json['id_imt'][5:]
        imt = request.json['imt']
        DataBase.create_db.add_imt_users(id_imt, imt)
    else:
        pass


@app.route('/change_imt', methods=['POST'])
def change_imt():
    id_imt = request.json['id_imt'][5:]
    new_imt = request.json['changed_imt']
    DataBase.create_db.change_imt(id_imt, new_imt)


@app.route('/chek', methods=['POST'])
def chek_imt_from_id():
    id_user = request.json[5:]
    imt_id_user = DataBase.create_db.chek_imt_id(id_user)
    if imt_id_user:
        return Response(status=300)
    else:
        return Response(status=200)


app.run()
