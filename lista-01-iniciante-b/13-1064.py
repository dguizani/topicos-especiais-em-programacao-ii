# -*- coding: utf-8 -*-

from statistics import mean

values = [
    x for x in [
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input())
    ] if x > 0
]

print(f"{len(values)} valores positivos")
print(f"{mean(values):.1f}")
