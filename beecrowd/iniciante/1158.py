# -*- coding: utf-8 -*-

n = int(input())

values = [[int(x) for x in input().split()] for _ in range(n)]

for x, y in values:
    if x % 2 == 0:
        x += 1
    
    soma = x
    
    for i in range(1, y):
        soma += x + 2 * i
    
    print(soma)
