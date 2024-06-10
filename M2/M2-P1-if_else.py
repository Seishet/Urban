first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Все числа равны: 3')
elif first == second or first == third or second == third:
    print('Два числа из трех равны: 2')
else:
    print('Равных чисел нет: 0')