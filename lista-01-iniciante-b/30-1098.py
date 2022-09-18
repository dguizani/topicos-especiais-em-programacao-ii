# -*- coding: utf-8 -*-

i = 0
j = k = 1

while i <= 2:
    for _ in range(3):
        print(f"I={i} J={j}")
        j += 1
    
    i = float(f"{(i + 0.2):.1f}")
    
    if ".0" in str(i):
        i = int(i)
    
    k = float(f"{(k + 0.2):.1f}")
    
    if ".0" in str(k):
        k = int(k)
    
    j = k
