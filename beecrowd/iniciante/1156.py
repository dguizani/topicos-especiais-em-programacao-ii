# -*- coding: utf-8 -*-

a = 1

values = []

for i in range(1, 40, 2):
    values.append(i / a)
    a *= 2

print(f"{sum(values):.2f}")
