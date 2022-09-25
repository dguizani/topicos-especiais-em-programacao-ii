# -*- coding: utf-8 -*-

caso = 1

while True:
    n, q = [int(x) for x in input().split()]
    
    if n == 0 and q == 0:
        break
    
    e_marmore = [int(input()) for _ in range(n)]
    q_consulta = [int(input()) for _ in range(q)]
    
    e_marmore.sort()
    
    print(f"CASE# {caso}:")
    
    for c in q_consulta:
        try:
            idx = e_marmore.index(c) + 1
        except ValueError:
            print(f"{c} not found")
            continue
        
        print(f"{c} found at {idx}")
    
    caso += 1
