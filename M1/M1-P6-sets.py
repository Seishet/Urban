my_dict = {'Tom':1974, 'Alex':2003, 'Max':1996 }
print('Dict:', my_dict)
print('Existing value:',my_dict['Tom'])
print('Not existing value:', my_dict.get('Rob'))
my_dict.update({'Kamila':1998, 'Mika':2004})
print('Deleted:', my_dict.pop('Tom'))
print(my_dict)
print()

my_set = {12, 'text', 25, True, 12, 3, 'type', True}
print(my_set)
my_set.update({6, 5.248})
print(my_set)
my_set.remove(True)
print(my_set)