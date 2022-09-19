# -*- coding: utf-8 -*-

from statistics import mean


values = []

while True:
    x = int(input())
    
    if x < 0:
        break
    
    values.append(x)

print(f"{mean(values):.2f}")
