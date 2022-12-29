# Задача 3 Семинар 2: Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
n = int(input('Введите число n: '))
result_list = {round((1+(1/i))**i, 2) for i in range(1, n+1)}
sum = 0
for i in result_list:
    sum += i
print(f'Сумма чисел в последовательности {result_list} - {sum}')