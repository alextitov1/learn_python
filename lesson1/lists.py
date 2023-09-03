#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_list = [3, 5, 7, 9, 10.5]
print(my_list)

my_list.append('Python')  # type: ignore
print(len(my_list))

print(my_list[0])
print(my_list[-1])
print(my_list[1:4])

my_list.remove('Python')  # type: ignore
print(my_list)
