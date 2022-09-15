# -*- coding: utf-8 -*-

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

a = (A * C) / 2
b = pi * (C ** 2)
c = ((A + B) * C) / 2
d = B ** 2
e = A * B

print(f"TRIANGULO: {a:.3f}")
print(f"CIRCULO: {b:.3f}")
print(f"TRAPEZIO: {c:.3f}")
print(f"QUADRADO: {d:.3f}")
print(f"RETANGULO: {e:.3f}")
