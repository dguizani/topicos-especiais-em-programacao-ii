# -*- coding: utf-8 -*-

qtd_notas = int(input())
atual = qtd_notas

notas_100 = atual // 100
atual -= notas_100 * 100

notas_50 = atual // 50
atual -= notas_50 * 50

notas_20 = atual // 20
atual -= notas_20 * 20

notas_10 = atual // 10
atual -= notas_10 * 10

notas_5 = atual // 5
atual -= notas_5 * 5

notas_2 = atual // 2
atual -= notas_2 * 2

notas_1 = atual

print(qtd_notas)
print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50,00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")
