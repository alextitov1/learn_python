# -*- coding: utf-8 -*-
"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def define_activity(age):
    if 0 <= age <= 6:
        return "You're a kindergartner"
    elif 7 <= age <= 17:
        return "You're a schoolboy"
    elif 18 <= age <= 23:
        return "You're a student"
    elif 24 <= age <= 65:
        return "You're a worker"
    elif 66 <= age <= 100:
        return "You're a retiree"
    else:
        return "You're probably dead"


def main():
    age = int(input('Pls enter your age: '))
    activity = define_activity(age)
    print(activity)


if __name__ == "__main__":
    main()
