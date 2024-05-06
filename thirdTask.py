"""
Задача 3. Написать функцию/метод, которая возвращает массив простых чисел в диапазоне
(2 числа - минимальное и максимальное) заданных чисел.
Например, на вход переданы 2 числа: от 11 до 20  (диапазон считается включая граничные значения).
На выходе программа должна выдать [11, 13 , 17, 19]
"""

from math import sqrt


def is_simple(n: int):
    divisors = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
    return True if len(divisors) == 0 else False


def generate_simple(min: int, max: int) -> list:
    simple_numbers = [i for i in range(min, max + 1) if is_simple(i)]
    return simple_numbers
