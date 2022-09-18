# -*- coding: utf-8 -*-

x = int(input()) # 2

a, b = 0, 1

fib = []

for i in range(x):
    fib += [str(a)]
    a, b = b, a + b

print(" ".join(fib))
