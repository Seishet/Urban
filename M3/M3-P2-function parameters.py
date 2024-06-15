def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 1 задание

print_params()
print_params(3, 25, [1,2,3])
print_params(34, 'text', )
print_params('text2')

#2 задание

values_list = ['tt', 23, False]
values_dict = {'a':33, 'b':True, 'c':22}
print()
print_params(*values_list)
print_params(**values_dict)

#3 задание

print()

values_list_2 = [22, 'param']
print_params(*values_list_2, 33)
print_params(14, *values_list_2)