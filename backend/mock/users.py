class User:
    def __init__(self, id, login, password, token=None):
        self.id = id
        self.login = login
        self.password = password
        self.token = token


user_1 = User(1, "Admin", "adminPassword")
user_2 = User(2, "User 2", "user 2 password")

users = [user_1, user_2]


def init_users():
    return users
