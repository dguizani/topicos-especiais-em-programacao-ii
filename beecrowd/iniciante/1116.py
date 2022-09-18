# -*- coding: utf-8 -*-

x = int(input())

values = [[int(k) for k in input().split()] for _ in range(x)]

for x, y in values:
    if y != 0:
        print(f"{(x / y):.1f}")
    else:
        print("divisao impossivel")
