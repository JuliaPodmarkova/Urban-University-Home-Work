class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """
    def __init__(self, username, password, confirm_password):
        self.username = username
        if password == confirm_password:
            self.password = password
class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password
if __name__ == '__main__':
    database = Database()
    user = User(input('Введите логин: '), input('Введите пароль: '), input('Повторите пароль: '))
    database.add_user(user.username, user.password)