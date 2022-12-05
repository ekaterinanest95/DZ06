# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from functools import reduce

n = int(input())
numbers = []

numbers = [float(input()) for i in range(n)]
print(f'Изначальный список: {numbers}')

numbers = list(map(lambda x: round(float(x) - int(x), 2), numbers))
print(f'Убираем целочисленную часть элементов: {numbers}')

numbers = list(filter(lambda x: float(x) != 0.0, numbers))
print(f'Список без элементов с нулевой дробной частью: {numbers}')

max_number = reduce(lambda x, y: x if (x > y) else y, numbers)
print(f'Максимальное значение: {max_number}')

min_number = reduce(lambda x, y: x if (x < y) else y, numbers)
print(f'Минимальное значение: {min_number}')

result = max_number - min_number
print(f'Разность максимального и минимального значений: {result}')
