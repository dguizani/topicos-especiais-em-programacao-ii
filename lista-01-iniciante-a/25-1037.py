# -*- coding: utf-8 -*-

v = float(input())

intervalo = "Fora de intervalo"

if 0 <= v <= 25:
    intervalo = "Intervalo [0,25]"
elif 25 < v <= 50:
    intervalo = "Intervalo (25,50]"
elif 50 < v <= 75:
    intervalo = "Intervalo (50,75]"
elif 75 < v <= 100:
    intervalo = "Intervalo (75,100]"

print(intervalo)
