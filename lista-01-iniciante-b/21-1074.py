# -*- coding: utf-8 -*-

n = int(input())

values = [int(input()) for _ in range(n)]

for v in values:
    x = ""
    
    if v == 0:
        x += "NULL"
    else:
        if v % 2 == 0:
            x += "EVEN"
        else:
            x += "ODD"
        
        if v > 0:
            x += " POSITIVE"
        else:
            x += " NEGATIVE"
    
    print(x)
