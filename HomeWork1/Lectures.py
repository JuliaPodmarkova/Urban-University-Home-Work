# Локальное, встроенное и глобальное пространство имен

def printer():
    global a, b
    a = 'Str'
    b = 'Str2'
    c = 15
    d = 20
    print(a, b, '- global')
    print(c, d, '- local')
printer()

# Способы вызова функции по умолчанию

def print_params(a, b, c):
    print(a, b, c, '- print param')
    print(a + c, '- summa 1 and 3 param')
print_params(1, 2,3)

def print_params(a = 1, b = 2, c = 3):
    print(a, b, c, '- print param')
    print(a + c, '- summa 1 and 3 param')
print_params(7)

def print_params(*, a, b, c):
    print(a, b, c, '- print param')
print_params(a = 1, b = 2, c = 3)

# Параметры по умолчанию внутри функции

def def_with_params(a, b):
    print(a + b)
def_with_params(1, 2)
def_with_params(4, 3)

def def_with_params(a = 1, b = 2):
    print(a + b)
def_with_params()
def_with_params(4, 3)

def def_with_params(a, b=2):
    print(a + b)
def_with_params(2)
def_with_params(4, 3)

def def_with_params(a, b=2, c=3):
    print(a + b + c)
def_with_params(1, 2)
def_with_params(4, 3, 5)

def def_with_params(a, b=2, c=[]):
    c.append(a)
    print(c)
def_with_params(3)
def_with_params(3)
def_with_params(3)

def def_with_params(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)
def_with_params(3)
def_with_params(3)
def_with_params(3)

# Распаковка позиционных параметров

def print_params(*args):
    print(args)
print_params(1, 2, 3, 4, 5, 6)

def print_params(*args):
    print(*args)
print_params(1, 2, 3, 4, 5, 6)

def print_params(a, b, c):
    print(a, b, c)
list_ = [1, 2, 3]
print_params(*list_)

def print_params(a, b, c):
    print(a, b, c)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    print(kwargs)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    for key in kwargs:
        print(key)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(a, b, c):
    print(a, b, c)
list_ = [1, 2]
dict_ = {'c': 3}
print_params(*list_, **dict_)