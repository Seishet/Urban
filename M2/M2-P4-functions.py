def get_matrix(n, m, value):
    matrix = []
    matrix = [[value for i in range(0, m)] for j in range(0, n)]
    return matrix


n_ = int(input('Введите количество строк: '))
m_ = int(input('Введите количество столбцов: '))
value_ = int(input('Введите элемент матрицы: '))

print(get_matrix(n_, m_, value_))


