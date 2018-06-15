import time
from mock.users import init_users
from mock.students import init_students


class Db:
    active_tokens = []

    def add_token(self, user_id):
        for u in self.users:
            if u.id == user_id:
                token = time.time()
                u.token = token
                self.active_tokens.append(token)
                return True
        return 'Новый токен не был зарегистрирован. Скорее всего пользователь с user_id ' + user_id + ' не был найден'

    def check_token(self, token):
        for t in self.active_tokens:
            if t == token:
                return True
            else:
                return 'Токен ' + token + ' не зарегистрирован в приложении'

    def remove_token(self, token):
        remove_from_user = False
        remove_from_active = False

        for t in self.active_tokens:
            if t == token:
                self.active_tokens.remove(t)
                remove_from_active = True
        for u in self.users:
            if u.token == token:
                u.token = None
                remove_from_user = True

        if remove_from_user & remove_from_active:
            return True
        else:
            return 'Удаление токена не произошло'

    users = init_users()

    def add_user(self, user):
        for u in self.users:
            if u.id == user.id:
                return 'Ошибка униакльности идентификатора при записи объекта user в БД'
            elif u.login == user.login:
                return 'Пользователь с таким именем уже зарегистрирован в системе'

        self.users.append(user)
        return True

    def get_user(self, id):
        for u in self.users:
            if u.id == id:
                return u
        return 'Пользователь с id ' + id + ' не найден'

    def get_users(self):
        return self.users

    def authorize_user(self, login, password):
        for u in self.users:
            if (u.login == login) & (u.password == password):
                return u
        return 'Пользователь с такой связкой login+password не найден'

    def remove_user(self, id):
        for u in self.users:
            if u.id == id:
                self.users.remove(u)
                return True
        return 'Пользователь с id ' + id + ' не удалён'

    students = init_students()

    def add_student(self, student):
        self.students.append(student)

    def get_student(self, id):
        for s in self.students:
            if s.id == id:
                return s
        return 'Студент с id ' + id + ' не найден'

    def get_students(self):
        return self.students

    def remove_student(self, id):
        for u in self.users:
            if u.id == id:
                self.users.remove(u)
                return
        return 'Студент с id ' + id + ' не удалён'
