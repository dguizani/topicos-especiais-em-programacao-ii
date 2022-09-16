# -*- coding: utf-8 -*-

A, B, C, D = [int(x) for x in input().split()]

cond = (
    B > C
    and D > A
    and C + D > A + B
    and C > 0
    and D > 0
    and A % 2 == 0
)

if cond:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
