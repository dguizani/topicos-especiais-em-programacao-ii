# -*- coding: utf-8 -*-

values = [
    x for x in [
        int(input()),
        int(input()),
        int(input()),
        int(input()),
        int(input())
    ] if x % 2 == 0
]

print(f"{len(values)} valores pares")
