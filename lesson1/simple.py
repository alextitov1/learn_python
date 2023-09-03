# -*- coding: utf-8 -*-
a = 2
b = 0.5
print(a + b)

name = 'Alex'
print(f'Hello, {name}!')

v = input('Введите число от 1 до 10: ')
print(int(v) + 10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

float('1')  # 1.0
# int('2.5') # ValueError: invalid literal for int() with base 10: '2.5'
bool(1)  # True
bool('')  # False
bool(0)  # False
