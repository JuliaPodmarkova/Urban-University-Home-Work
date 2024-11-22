from random import choice
from tkinter.ttk import Style

from Module5. import

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
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print('Вход выполнен.')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password != password2:
                print("Пароли не совпадают")
                continue
            if check_password(password) != 1:
                print("Пароль не соответствует минимальным критериям: длина 8 символов, одна цифра, одна заглавная и одна прописная буквы")
                continue
            database.add_user(user.username, user.password)
        print(database.data)

