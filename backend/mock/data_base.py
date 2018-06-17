import time

from mock.users import init_users
from mock.students import init_students


class ProcedureResult:
    def __init__(self, procedure,  is_success, message=None, result=None):
        self.procedure = procedure
        self.is_success = is_success
        self.message = message
        self.result = result

    def to_json(self):
        return {
            'procedure': self.procedure,
            'isSuccess': self.is_success,
            'message': self.message,
            'result': self.result,
        }

    def __repr__(self):
        return str(self.to_json())


class Db:
    active_tokens = ['69']

    def add_token(self, user_id):
        for u in self.users:
            if u.id == user_id:
                if u.token is None:
                    token = str(time.time())
                    u.token = token
                    self.active_tokens.append(token)
                    return ProcedureResult('add_token', True, None, u)
                else:
                    return ProcedureResult('add_token', False, 'У пользователя ' + u.login + ' уже есть активный токен')
        return ProcedureResult('add_token', False, 'Новый токен не был зарегистрирован. Скорее всего пользователь с user_id ' + user_id + ' не был найден')

    def check_token(self, token):
        for t in self.active_tokens:
            if t == token:
                return ProcedureResult('check_token', True)
        return ProcedureResult('check_token', False, 'Токен ' + token + ' не зарегистрирован в приложении')

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
            return ProcedureResult('remove_token', True)
        else:
            return ProcedureResult('remove_token', False, 'Удаление токена не произошло')

    users = init_users()

    def add_user(self, user):
        for u in self.users:
            if u.id == user.id:
                return ProcedureResult('add_user', False, 'Ошибка униакльности идентификатора при записи объекта user в БД')
            elif u.login == user.login:
                return ProcedureResult('add_user', False, 'Пользователь с таким именем уже зарегистрирован в системе')

        self.users.append(user)
        return ProcedureResult('add_user', True)

    def get_user(self, value, by='id'):
        for u in self.users:
            if u.get(by) == value:
                return ProcedureResult('get_user', True, None, u)
        return ProcedureResult('get_user', False, 'Пользователь с ' + by + '=' + value + ' не найден')

    def get_users(self):
        if len(self.users) > 0:
            return ProcedureResult('get_users', True, None, self.users)
        else:
            return ProcedureResult('get_users', False, 'Список users пуст')

    def authorize_user(self, login, password):
        for u in self.users:
            if (u.login == login) & (u.password == password):
                return ProcedureResult('authorize_user', True, None, u)
        return ProcedureResult('authorize_user', False, 'Пользователь с такой связкой login+password не найден')

    def remove_user(self, id):
        for u in self.users:
            if u.id == id:
                self.users.remove(u)
                return ProcedureResult('remove_user', True)
        return ProcedureResult('remove_user', False, 'Пользователь с id ' + id + ' не удалён')

    students = init_students()

    def add_student(self, student):
        for s in self.students:
            if s.id == student.id:
                return ProcedureResult('add_student', False, 'Ошибка униакльности идентификатора при записи объекта student в БД')

        self.students.append(student)
        return ProcedureResult('add_student', True)

    def get_student(self, id):
        for s in self.students:
            if str(s.id) == str(id):
                return ProcedureResult('get_student', True, None, s)
        return ProcedureResult('get_student', False, 'Студент с id ' + id + ' не найден')

    def get_students(self):
        if len(self.students) > 0:
            return ProcedureResult('get_students', True, None, self.students)
        else:
            return ProcedureResult('get_students', False, 'Список students пуст')

    def remove_student(self, id):
        for u in self.users:
            if u.id == id:
                self.users.remove(u)
                return ProcedureResult('remove_student', True)
        return ProcedureResult('remove_student', False, 'Студент с id ' + id + ' не удалён')
