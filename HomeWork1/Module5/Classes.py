class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.say_info()
        self.birthday()
        self.__del__()
        self.__len__()



    def say_info(self):
            print(f'Привет, меня зовут {self.name} {self.surname}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')
        if self.age >= 18:
            print(f'Я достиг возраста, когда можно получить водительское удостоверение')

    def __del__(self):
        print(f'{self.name} ушёл')

    def __len__(self):
        return self.age

    def __lt__(self, other):
         return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __str__(self):
        return f'{self.name} {self.surname}'

den = Human("Denis", 0,15)
max = Human("Maxim", 0,22)

den.surname = "Popov"
den.age = 17
max.surname = "Petrov"
#print(den.name, den.surname, den.age)
#print(max.name, max.age)
print(den)
print(max)
#print(max < den)
#print(max > den)
#print(max == den)
print(den != max)
#max.birthday
#del(max)
#print(len(den))
#input()