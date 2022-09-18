# -*- coding: utf-8 -*-

values = []

while True:
    val = [int(v) for v in input().split()]
    val.sort()
    
    x, y = val
    
    if x <= 0 or y <= 0:
        break
    
    values.append([v for v in range(x, y + 1)])

for v in values:
    print(" ".join([f"{x}" for x in v]), f"Sum={sum(v)}")
