# -*- coding: utf-8 -*-

from cmath import sqrt


A, B, C = [float(x) for x in input().split()]

div = 2 * A
delta = B ** 2 - 4 * A * C

if delta < 0 or div == 0:
    print("Impossivel calcular")
else:
    r_delta = sqrt(delta).real

    x_ = (-B + r_delta) / div
    x__ = (-B - r_delta) / div

    print(f"R1 = {x_:.5f}")
    print(f"R2 = {x__:.5f}")
