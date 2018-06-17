from flask import jsonify


class User:
    def __init__(self, id, login, password, token=None):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

    def get(self, what):
        if what == 'token':
            return self.token
        elif what == 'id':
            return self.id
        else:
            return self

    def to_json(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password,
            "token": self.token
        }

    def __repr__(self):
        return str(self.to_json())


# account with token fo call test API GET request
user_1 = User(0, "Admin", "adminPassword", "69")
# account to quick login
user_2 = User(1, "1", "1")
user_3 = User(2, "login", "password")

users = [user_1, user_2, user_3]


def init_users():
    return users
