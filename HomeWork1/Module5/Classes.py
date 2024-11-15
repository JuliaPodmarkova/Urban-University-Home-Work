class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

den = Human("Denis", 15)
max = Human("Maxim", 22)
den.surname = "Popov"
den.age = 17
max.surname = "Petrov"

print(den.name, den.surname, den.age)
print(max.name, max.age)

def say_info(self):
    print(f'Привет, меня зовут {self.name} {self.surname}, мне {self.age}')

say_info(max)

def birthday(self):
    self.age += 1
    print(f'У меня день рождения, мне теперь {self.age}')
    if self.age >= 18:
        print(f'Я достиг возраста, когда можно получить водительское удостоверение')
birthday(den)
