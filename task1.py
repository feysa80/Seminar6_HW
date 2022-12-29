# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
input_ex = input('Введите арифметическое выражение: ')
num = input_ex.split()
while len(num) > 1:
    while '*' in num or '/' in num:
        for i in num:
            if i == '*':
                num[num.index('*') - 1] = float(num[num.index('*') - 1]) * float(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            elif i == '/':
                num[num.index('/') - 1] = float(num[num.index('/') - 1]) / float(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
    while '+' in num or '-' in num:
        if '+' in num:
            num[num.index('+') - 1] = float(num[num.index('+') - 1]) + float(num[num.index('+') + 1])
            num.pop(num.index('+') + 1)
            num.pop(num.index('+'))
        else:
            num[num.index('-') - 1] = float(num[num.index('-') - 1]) - float(num[num.index('-') + 1])
            num.pop(num.index('-') + 1)
            num.pop(num.index('-'))
result = round(num[0], 3)
print(result)
