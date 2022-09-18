# -*- coding: utf-8 -*-

def nota_valida(nota: float):
    return 0 <= nota <= 10


while True:
    nota_1 = float(input())
    
    if nota_valida(nota_1):
        break
    
    print("nota invalida")

while True:
    nota_2 = float(input())
    
    if nota_valida(nota_2):
        break
    
    print("nota invalida")

media = (nota_1 + nota_2) / 2

print(f"media = {media:.2f}")
