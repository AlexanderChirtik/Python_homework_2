#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

Number = int(input("Введите число "))
list = []
i = 1
while (Number >= i):
    list.append(round((1+1/i) ** i, 2))
    i += 1
sum = 0
for i in range(0, Number):
    print(f'{i + 1}: {list[i]} ')
    sum += list[i]
print(f'Сумма равна {sum}')
