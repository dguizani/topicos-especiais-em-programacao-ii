# -*- coding: utf-8 -*-

x = int(input())

if x % 2 == 0:
    x += 1

for i in range(6):
    print(x + i * 2)
