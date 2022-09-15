# -*- coding: utf-8 -*-

N = int(input())

A = N // 365
M = (N % 365) // 30
D = (N % 365) % 30

print(f"{A} ano(s)")
print(f"{M} mes(es)")
print(f"{D} dia(s)")
