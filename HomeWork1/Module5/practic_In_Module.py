from random import choice

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

def check_password(password):
    if len(password) < 8: #Длинна пароля
        return False
    if not any(char.isupper() for char in password): #Наличие хотя бы 1ой заглавной буквы
        return False
    if not any(char.islower() for char in password): #Наличие хотя бы 1ой буквы в нижнем регистре
        return False
    if not any(char.isdigit() for char in password): #Наличие хотя бы 1ой цифры
        return False
    return True

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n')
        user = User(input('Введите логин: '), password := input('Введите пароль: '), password2 := input('Повторите пароль: '))
        if password != password2:
            exit("Пароли не совпадают")
        if check_password(password) != 1:
            exit("Пароль не соответствует минимальным критериям: длина 8 символов, одна цифра, одна заглавная и одна прописная буквы")
        database.add_user(user.username, user.password)
        print(database.data)

