# coding=utf-8
import sys
x = input("a: ")
y = input("b: ")

def func(var_a, var_b):
    if isinstance(var_a, str) or isinstance(var_b, str):
        return 'str'
    elif var_a > var_b:
        return '>'
    elif var_a == var_b:
        return '='
    else:
        return '<'
print(func(x, y))
