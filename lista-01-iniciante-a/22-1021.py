# -*- coding: utf-8 -*-

valor = float(input())
notas = int(valor)
moedas = valor - notas

notas_100 = notas // 100
notas -= notas_100 * 100

notas_50 = notas // 50
notas -= notas_50 * 50

notas_20 = notas // 20
notas -= notas_20 * 20

notas_10 = notas // 10
notas -= notas_10 * 10

notas_5 = notas // 5
notas -= notas_5 * 5

notas_2 = notas // 2
notas -= notas_2 * 2

moedas_100 = notas // 1
notas -= moedas_100 * 1

moedas = float(f"{moedas:.2f}")

moedas_050 = moedas // 0.50
moedas -= moedas_050 * 0.50

moedas = float(f"{moedas:.2f}")

moedas_025 = moedas // 0.25
moedas -= moedas_025 * 0.25

moedas = float(f"{moedas:.2f}")

moedas_010 = moedas // 0.10
moedas -= moedas_010 * 0.10

moedas = float(f"{moedas:.2f}")

moedas_005 = moedas // 0.05
moedas -= moedas_005 * 0.05

moedas = float(f"{moedas:.2f}")

moedas_001 = moedas // 0.01
moedas -= moedas_001 * 0.01

moedas = float(f"{moedas:.2f}")

if moedas == 0.01:
    moedas_001 += 1

print("NOTAS:")
print(f"{notas_100:.0f} nota(s) de R$ 100.00")
print(f"{notas_50:.0f} nota(s) de R$ 50.00")
print(f"{notas_20:.0f} nota(s) de R$ 20.00")
print(f"{notas_10:.0f} nota(s) de R$ 10.00")
print(f"{notas_5:.0f} nota(s) de R$ 5.00")
print(f"{notas_2:.0f} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedas_100:.0f} moeda(s) de R$ 1.00")
print(f"{moedas_050:.0f} moeda(s) de R$ 0.50")
print(f"{moedas_025:.0f} moeda(s) de R$ 0.25")
print(f"{moedas_010:.0f} moeda(s) de R$ 0.10")
print(f"{moedas_005:.0f} moeda(s) de R$ 0.05")
print(f"{moedas_001:.0f} moeda(s) de R$ 0.01")
