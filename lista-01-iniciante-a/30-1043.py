# -*- coding: utf-8 -*-

a, b, c = [float(x) for x in input().split()]

if a < b + c and b < a + c and c < a + b:
    print(f"Perimetro = {a + b + c}")
else:
    print(f"Area = {(a + b) * c / 2.0}")
