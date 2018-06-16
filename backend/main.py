from flask import request, jsonify

from app import app
from mock.data_base import Db
from mock.users import User
from mock.students import Student

db = Db()


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(len(db.users), data['login'], data['password'])
    register_result = db.add_user(new_user)

    if not register_result.is_success:
        return jsonify(register_result)

    return login()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    authorize_result = db.authorize_user(data['login'], data['password'])

    if not authorize_result.is_success:
        return jsonify(authorize_result)

    return jsonify(db.add_token(authorize_result.result.id))


@app.route('/logout', methods=['POST'])
def log_out():
    data = request.get_json()
    logout_result = db.remove_token(data['token'])

    return jsonify(logout_result)


@app.route('/leave/<string:token>', methods=['DELETE'])
def delete_user(token):
    print(token)
    user_result = db.get_user(token, 'token')

    if not user_result.is_success:
        return jsonify(user_result)

    return jsonify(db.remove_user(user_result.result.id))


@app.route('/users/<string:token>', methods=['GET'])
def get_users(token):
    # token = token="1234567890"&
    # todo: take get parameter value by another way
    check_result = db.check_token(token[7:-2])

    if not check_result.is_success:
        return jsonify(check_result)

    return jsonify(db.get_users())


@app.route('/user/<string:token>&<id>', methods=['GET'])
def get_user(token, id):
    # token = token="1234567890"&
    # id = id="1234567890"&
    # todo: take get parameter value by another way
    check_result = db.check_token(token[7:-1])

    if not check_result.is_success:
        return jsonify(check_result)

    return jsonify(db.get_user(id[4:-2]))

@app.route('/students/<string:token>', methods=['GET'])
def get_students(token):
    # token = token="1234567890"&
    # todo: take get parameter value by another way
    check_result = db.check_token(token[7:-2])

    if not check_result.is_success:
        return jsonify(check_result)

    return jsonify(db.get_students())


@app.route('/student/<string:token>&<id>', methods=['GET'])
def get_student(token, id):
    # token = token="1234567890"&
    # id = id="1234567890"&
    # todo: take get parameter value by another way
    check_result = db.check_token(token[7:-1])

    if not check_result.is_success:
        return jsonify(check_result)

    return jsonify(db.get_student(id[4:-2]))


@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(len(db.students), data['name'], data['info'])
    save_result = db.add_student(new_student)

    return jsonify(save_result)


@app.route('/student/<token>&<id>', methods=['DELETE'])
def delete_student(token, id):
    return 'student: {...}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
