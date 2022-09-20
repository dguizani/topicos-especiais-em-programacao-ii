# -*- coding: utf-8 -*-

def truncate(n, c):
    return int(n * 10 ** c) / 10 ** c


qt_cidades = 0

while True:
    n = int(input())
    
    if n == 0:
        break
    
    qt_cidades += 1
    
    soma_pessoas = 0
    soma_consumo = 0
    
    values = []
    
    for _ in range(n):
        x, y = [int(k) for k in input().split()]
        soma_pessoas += x
        soma_consumo += y
        
        values += [[x, y // x]]
    
    values.sort(key=lambda x: x[1])
    
    media = soma_consumo / soma_pessoas

    if qt_cidades > 1:
        print()

    print(f"Cidade# {qt_cidades}:")

    for v in values:
        print("-".join([str(x) for x in v]), end=" ")

    print(f"\b\nConsumo medio: {truncate(media, 2)} m3.")
