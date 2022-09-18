# -*- coding: utf-8 -*-

x = int(input())

values = [[float(i) for i in input().split()] for _ in range(x)]

pesos = [2, 3, 5]
sum_pesos = sum(pesos)

for n1, n2, n3 in values:
    media = (
        n1 * pesos[0]
        + n2 * pesos[1]
        + n3 * pesos[2]
    )
    
    media /= sum_pesos
    
    print(f"{media:.1f}")
