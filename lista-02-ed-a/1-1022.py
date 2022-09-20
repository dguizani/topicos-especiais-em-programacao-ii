# -*- coding: utf-8 -*-

from math import gcd


x = int(input())

expressoes = [
    [
        int(x)
        if i % 2 == 0
        else x
        for i, x in enumerate(input().split())
    ] for _ in range(x)
]

res = []

for n1, div1, d1, oper, n2, div2, d2 in expressoes:
    calc = {
        "+": [(n1 * d2 + n2 * d1), "/", (d1 * d2)],
        "-": [(n1 * d2 - n2 * d1), "/", (d1 * d2)],
        "*": [(n1 * n2), "/", (d1 * d2)],
        "/": [(n1 * d2), "/", (n2 * d1)]
    }
    
    numerador, c, denominador = calc.get(oper)
    
    mdc = gcd(numerador, denominador)
    
    append = (
        [str(numerador), c, str(denominador)],
        [str(numerador // mdc), c, str(denominador // mdc)]
    )
    
    res.append(append)

for num, den in res:
    print(f"{''.join(num)} = {''.join(den)}")
