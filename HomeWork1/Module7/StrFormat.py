# конкатенация (сложение строк)
print('Hello ' + 'word')
print('This' + ' is ' + 'the ' + str(14) + ' character') # складывать можно только строку со строкой, поэтому,
# например числа, необходимо переводить в строку, иначе будет возникать ошибка компиляции
print('Привет! Меня зовут %s, мне %s лет' % ('Юлия', 38)) # форматирование строки с использованием символа %
# и кортежа.
# Также вместо «%s» можно использовать «%d» (но при использовании строкового значения возникнет ошибка) и
# «%x» (число переводится в строковое представление в шестнадцатеричном формате). Этот метод использовать не стоит,
# поскольку он устарел, однако его можно встретить в старых примерах кода. Также можно увидеть вариант, когда
# после знака «%» добавляются скобки и значения. Это похоже на именованные параметры, и здесь кортеж не подойдет
print('Моего кота зовут %(name)s, он %(color)s цвета с %(color2)s пятнами.' % {'name': 'Lucky',
                                                        'color': 'черного', 'color2': 'белыми'})
# новый метод вместо %s
print('Я учусь в {}'.format('Urban'))
print('Я учусь в {} {}'.format('Urban', 'university'))
print('Я учусь в {title} – {postfix} {title}'.format(title = "Urban", postfix = "university"))
print(f'{"Urban"} это лучший университет')