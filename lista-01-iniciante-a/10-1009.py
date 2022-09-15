# -*- coding: utf-8 -*-

nome = input()
sal_fixo = float(input())
tot_vendas = float(input())

comissao = 0.15 * tot_vendas

tot_sal = sal_fixo + comissao

print(f"TOTAL = R$ {tot_sal:.2f}")
