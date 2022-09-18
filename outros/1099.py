# -*- coding: utf-8 -*-

n = int(input())

values = [[int(x) for x in input().split()] for _ in range(n)]

[x.sort() for x in values]

for x, y in values:
    impares = [v for v in range(x + 1, y) if v % 2 != 0]
    sum_impares = sum(impares)
    print(sum_impares)
