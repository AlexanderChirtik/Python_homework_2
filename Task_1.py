#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Number = input("Введите число ")
sum_of_numbers = 0
for i in Number:
    if (i == "," or i == "."):
        sum_of_numbers += 0
    else:
        sum_of_numbers += int(i)
print(sum_of_numbers)