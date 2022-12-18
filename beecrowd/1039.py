# -*- coding: utf-8 -*-

import math


while True:
    try:
        r1, x1, y1, r2, x2, y2 = [int(x) for x in input().split()]
    except:
        break
    
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    if r1 >= d + r2:
        print("RICO")
    else:
        print("MORTO")
