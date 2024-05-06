"""
Задача 4. Написать метод, который в консоль выводит таблицу умножения.
На вход метод получает число, до которого выводит таблицу умножения.
В консоли должна появиться таблица. Например, если на вход пришло число 5, то получим:
"""

def print_table(number: int) -> None:
    ln = len(str(number))
    max_count = len(str(number ** 2)) + 1
    print(" " * ln, end="")
    for i in range(1, number + 1):
        print(str(i).rjust(max_count), end="")
    print()
    for i in range(1, number + 1):
        print(str(i).ljust(ln), end="")
        for j in range(1, number + 1):
            print(str(i * j).rjust(max_count), end="")
        print()


print_table(25)