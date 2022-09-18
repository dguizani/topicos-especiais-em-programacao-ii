# -*- coding: utf-8 -*-

def nota_valida():
    while True:
        nota = float(input())
        
        if 0 <= nota <= 10:
            return nota
        
        print("nota invalida")


def sair():
    while True:
        sair = int(input("novo calculo (1-sim 2-nao)\n"))
        
        if sair not in (1, 2):
            continue
        
        return sair == 2


while True:
    nota_1, nota_2 = nota_valida(), nota_valida()

    media = (nota_1 + nota_2) / 2

    print(f"media = {media:.2f}")

    if sair():
        break
