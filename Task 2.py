# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


Number = int(input("Введите число "))
multi = 1
count = 1
list = []
while (Number > 0):
     multi *= count
     list.append(multi)
     count +=1
     Number -= 1
print(list)