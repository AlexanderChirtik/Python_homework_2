# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном списке
import random

Number = int(input("Введите число "))
list1 = []
for i in range(Number):
    list1.append(random.randint(-Number, Number))

list2 = []
for j in range(random.randint(2, Number)):
    variable = random.randint (0, Number - 1)
    if (list2.count(variable) == 0):
        list2.append(variable)
print(f'Список {list1}')
print(f'Индексы элементов, которые нужно умножить {list2}')
multi = 1
for l in list2:
    multi *= list1[l]
print(f'Произведение элементов на указанных индексах = {multi}')
