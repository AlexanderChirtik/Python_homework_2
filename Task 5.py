# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
import random

list = []
lenght = 6
for i in range (lenght):
    list.append(random.randint(0, 10))
print(list)

first_index = random.randint(0, lenght - 1)
second_index = random.randint(0, lenght - 1)
if (first_index != second_index):
    temp = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = temp
else:
    while (first_index == second_index):
        first_index = random.randint(0, lenght - 1)
    temp = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = temp
print(list)