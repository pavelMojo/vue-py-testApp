from flask import Flask, request, jsonify

from request_utils import request_response
from mock.data_base import Db
from mock.users import User
from mock.students import Student

app = Flask(__name__)
db = Db()


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(db.users.count, data['login'], data['password'])
    register_result = db.add_user(new_user)

    if isinstance(register_result, str):
        return request_response(register_result, True)

    login()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print("data из login :", data)
    authorize_result = db.authorize_user(data['login'], data['password'])

    if isinstance(authorize_result, str):
        return request_response(authorize_result, True)

    permission_result = db.add_token(authorize_result.id)

    if isinstance(permission_result, str):
        return request_response(authorize_result, True)

    return request_response()


@app.route('/logout', methods=['POST'])
def log_out():
    data = request.get_json()
    authorize_result = db.authorize_user(data['login'], data['password'])

    if isinstance(authorize_result, str):
        return request_response(authorize_result, True)

    logout_result = db.remove_token(authorize_result.token)

    if isinstance(logout_result, str):
        return request_response(logout_result, True)

    return request_response()

@app.route('/students', methods=['GET'])
def get_students():
    data = request.get_json()
    print('обработчик запроса')
    print('data', data)
    print(db.students)
    return request_response('/students response')
    #если такой токен есть у пользователй, отправляем список студентов?
    #если нет, отправляем ошибку
    #return 'students: {...}'

@app.route('/student/<token>&<id>', methods=['GET'])
def get_student(token, id):
    return 'student: {...}'

@app.route('/student/<token>&<id>', methods=['DELETE'])
def delete_student(token, id):
    return 'student: {...}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
