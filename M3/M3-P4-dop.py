def calculate_structure_sum(param):
    sum = 0

    if len(param) == 0:
        return sum
    else:
        for i in param:
            if isinstance(i, list):
                sum += calculate_structure_sum(i)
            elif isinstance(i, dict):
                sum += calculate_structure_sum(i.keys())
                sum += calculate_structure_sum(i.values())
            elif isinstance(i, tuple):
                sum += calculate_structure_sum(i)
            elif isinstance(i, set):
                sum += calculate_structure_sum(i)
            else:
                if type(i) == int:
                   sum += int(i)
                elif type(i) == str:
                    sum += len(i)
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
