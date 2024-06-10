immutable_var = 2, 'text', True
print(immutable_var)

#immutable_var[0] = 26
#print(immutable_var)
#immutable_var - это кортеж, который является неизменяемым типом данных
#обращение по индексу и замена значения невозможна, пэтому получим ошибку.
#Можно менять длинну кортежа за счет умножение или сложения,
#но нельзя изменять уже записанные данные


mutable_list = [12, 15, 20, 'text']
print(mutable_list)
mutable_list[1] = 26
print(mutable_list)