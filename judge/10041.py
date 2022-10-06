# -*- coding: utf-8 -*-

qtt_casos = int(input())

for _ in range(qtt_casos):
    caso_teste = [int(x) for x in input().split()][1:]
    caso_teste.sort()
    
    casas = []
    
    for c in caso_teste:
        ds = []
        
        for c2 in caso_teste:
            ds.append(abs(c - c2))
        
        casas.append(sum(ds))

    print(min(casas))
