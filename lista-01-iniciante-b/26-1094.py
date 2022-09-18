# -*- coding: utf-8 -*-

x = int(input())

values = [input().split() for _ in range(x)]

total = 0
total_c = 0
total_r = 0
total_s = 0

for qt, tipo in values:
    qt = int(qt)
    total += qt
    
    if tipo == "C":
        total_c += qt
    elif tipo == "R":
        total_r += qt
    else:
        total_s += qt

percent_c = (total_c * 100) / total
percent_r = (total_r * 100) / total
percent_s = (total_s * 100) / total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_c}")
print(f"Total de ratos: {total_r}")
print(f"Total de sapos: {total_s}")
print(f"Percentual de coelhos: {percent_c:.2f} %")
print(f"Percentual de ratos: {percent_r:.2f} %")
print(f"Percentual de sapos: {percent_s:.2f} %")
