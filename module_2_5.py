# Домашняя работа по уроку "Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    # Создаем пустую матрицу размером n x m
    matrix = []
    for i in range(n):
        matrix_line = []
        for j in range(m):
            matrix_line.append(value)
        matrix.append(matrix_line)

    return matrix

result1 = get_matrix(2, 2, 10)

result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
