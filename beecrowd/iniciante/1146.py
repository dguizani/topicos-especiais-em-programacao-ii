# -*- coding: utf-8 -*-

while True:
    x = int(input())
    
    if x == 0:
        break
    
    print(" ".join(str(k) for k in range(1, x + 1)))
