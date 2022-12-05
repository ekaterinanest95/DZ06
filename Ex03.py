# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from functools import reduce

number = list(input('Введите вещественное число: '))
sum_of_digits = 0

number = list(filter(lambda x: x not in (',', '.'), number))
print(f'Введенное число: {number}')

sum_of_digits = reduce(lambda x, y: int(x) + int(y), number)
print(f'Сумма цифр числа: {sum_of_digits}')
