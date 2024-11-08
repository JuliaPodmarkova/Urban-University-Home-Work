# использование данных из модуля (листа *.py)
import lists as li
import defen as de
from module_2_3 import my_list
from module_1_4 import *
print(dir(li))
print()
print(li.food)
print()
de.twoDayLottery('Monday', 'Tusdey')
print()
print(my_list)
print()
print(my_string)