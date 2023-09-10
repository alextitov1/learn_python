# -*- coding: utf-8 -*-
"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == 'learn':
        return 3
    return 'Something went wrong'


def main():
    print(compare_strings('Hello', 'Hello'))
    print(compare_strings('Hello', 'Hello world'))
    print(compare_strings('Hello', 'learn'))
    print(compare_strings('Hello', 123))


if __name__ == "__main__":
    main()
