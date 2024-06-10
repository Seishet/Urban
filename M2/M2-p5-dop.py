n = int(input('Введите число из первой вставки: '))
while n < 3 or n > 20:
    print('Неправильно заданное число. Число должно быть в диапазоне от 3 до 20')
    n = int(input('Введите число из первой вставки,: '))

result_pass = []

for i in range(1, 20):
    for j in range(i + 1, 20):
        if n % ( i + j ) == 0:
            result_pass.append(i)
            result_pass.append(j)


print(result_pass)