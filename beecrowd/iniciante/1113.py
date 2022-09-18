# -*- coding: utf-8 -*-

values = []

while True:
    x, y = [int(v) for v in input().split()]
    
    if x == y:
        break
    
    values.append(
        "Crescente"
        if x < y
        else "Decrescente"
    )

print("\n".join(values))
