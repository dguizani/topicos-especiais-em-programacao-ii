# -*- coding: utf-8 -*-

qt_positivo = len([
    x for x in [
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input()),
        float(input())
    ] if x > 0
])

print(f"{qt_positivo} valores positivos")
