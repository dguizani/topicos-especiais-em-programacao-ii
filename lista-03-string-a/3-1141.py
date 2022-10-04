# -*- coding: utf-8 -*-

while True:
    n = int(input())
    
    if n == 0:
        break
    
    values = [input() for _ in range(n)]
    
    for v in values:
        count = 0
        for i, c in enumerate(v[1:]):
            count += 1
            
            print(i, c)
            
            if not v[i] == chr(ord(c) - 1):
                break
        
        print(count)
