# -*- coding: utf-8 -*-

from cmath import sqrt


x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]

d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)).real

print(f"{d:.4f}")
