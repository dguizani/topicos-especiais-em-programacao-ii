# -*- coding: utf-8 -*-

import datetime as dt


di = int(input().split()[1])

hi, mi, si = [int(x) for x in input().split(" : ")]

df = int(input().split()[1])

hf, mf, sf = [int(x) for x in input().split(" : ")]

data_inicio = dt.datetime(1, 1, di, hi, mi, si)

data_fim = dt.datetime(1, 1, df, hf, mf, sf)

duracao = data_fim - data_inicio

dia = duracao.days

minuto, segundo = divmod(duracao.seconds, 60)
hora, minuto = divmod(minuto, 60)

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")
