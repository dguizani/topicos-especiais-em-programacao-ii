# -*- coding: utf-8 -*-

A, B, C = [int(x) for x in input().split()]

maior = (A + B + abs(A - B)) / 2
maior = (maior + C + abs(maior - C)) / 2

print(f"{maior:.0f} eh o maior")
