import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[:2, 1:3])


matrix = np.arange(1, 26).reshape(5, 5)

part1 = matrix[:3, :]
print("Первые три строки:\n", part1, "\nshape:", part1.shape)

part2 = matrix[-2:, :]
print("Последние две строки:\n", part2, "\nshape:", part2.shape)

part3 = matrix[:, :2]
print("Первые два столбца:\n", part3, "\nshape:", part3.shape)

part4 = matrix[1:4, 2:5]
print("Строки 1–3 и столбцы 2–4:\n", part4, "\nshape:", part4.shape)

part5 = matrix[-2:, -2:]
print("Угловой блок 2x2 в правом нижнем углу:\n", part5, "\nshape:", part5.shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# .copy() создаёт независимую копию данных, а без него изменения в changed_hours затронули бы исходный массив hours
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
