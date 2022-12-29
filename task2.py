# Задача 2 Семинар 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число N: '))
n_list = [i for i in range(1, n+1)]
for i in range(1, n):
    n_list[i] *= n_list[i-1]
print(n_list)