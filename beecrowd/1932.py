# -*- coding: utf-8 -*-

def input_int():
    return [int(x) for x in input().split()]


def lucro_maximo(bolsa: list[int], dias: int, taxa: int):
    l_atual = l_final = bolsa[0]
    l_maximo = 0
    
    for vb in bolsa[1:dias]:
        if (
            (
                l_atual > vb
                and l_atual - vb >= taxa
            ) or (
                vb < l_final
            )
        ):
            if l_atual - l_final - taxa > 0:
                l_maximo += l_atual - l_final - taxa
            
            l_atual = l_final = vb
        
        if vb > l_atual:
            l_atual = vb

    if l_atual - l_final - taxa > 0:
        l_maximo += l_atual - l_final - taxa
    
    return l_maximo


dias, taxa = input_int()

bolsa = input_int()

print(lucro_maximo(bolsa, dias, taxa))
