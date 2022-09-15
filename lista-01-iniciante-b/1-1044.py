# -*- coding: utf-8 -*-

v1, v2 = input().split()

if float(v2) % float(v1) == 0 or float(v1) % float(v2) == 0:
    print("Sao Multiplos")
else:
    print("Nao Sao Multiplos")
