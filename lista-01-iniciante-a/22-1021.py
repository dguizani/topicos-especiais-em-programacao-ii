# -*- coding: utf-8 -*-

v = float(input())

notas = (100, 50, 20, 10, 5, 2)

moedas = (1, .50, .25, .10, .05, .01)

print("NOTAS:")
for n in notas:
    q_notas = v // n
    print(f"{q_notas:.0f} nota(s) de R$ {n:.2f}")
    v -= q_notas * n

print("MOEDAS:")
for m in moedas:
    q_moedas = v // m
    print(f"{q_moedas:.0f} moeda(s) de R$ {m:.2f}")
    v -= q_moedas * m
