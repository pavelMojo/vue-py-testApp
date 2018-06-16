from flask import jsonify


class User:
    def __init__(self, id, login, password, token=None):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

    def to_json(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password,
            "token": self.token
        }

    def __repr__(self):
        return str(self.to_json())


user_1 = User(0, "Admin", "adminPassword")
user_2 = User(1, "User 2", "user 2 password")

users = [user_1, user_2]


def init_users():
    return users
