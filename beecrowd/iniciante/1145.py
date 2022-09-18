# -*- coding: utf-8 -*-

x, y = [int(k) for k in input().split()]

for i in range(1, y + 1):
    print(i, end=("\n" if i % x == 0 else " "))
