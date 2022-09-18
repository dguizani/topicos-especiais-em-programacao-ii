# -*- coding: utf-8 -*-

values = [
    int(input()),
    int(input())
]

values.sort()

x, y = values

x += 1

if x % 2 == 0:
    x += 1

print(sum(range(x, y, 2)))
