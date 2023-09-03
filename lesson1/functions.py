# -*- coding: utf-8 -*-
def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'


print(get_summ('Learn', 'python').upper())
