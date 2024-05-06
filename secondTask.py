"""
Задача 2. Написать функцию/метод, которая на вход получает массив положительных целых чисел произвольной длины. 
Например [42, 12, 18]. На выходе возвращает массив чисел, которые являются общими делителями для всех указанных числе.
В примере это будет [2, 3, 6].
"""

from typing import List
from math import sqrt


def find_divisors(n: int):
    divisors = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
    return divisors


def find_divisors_array(numbers: List[int]) -> List[int]:
    temp_a = [find_divisors(i) for i in numbers]
    out = [temp_a[0] & temp_a[i] for i in range(1, len(temp_a))][0]
    return list(out)
