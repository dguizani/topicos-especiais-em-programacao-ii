# -*- coding: utf-8 -*-

tabela = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

cod, qt = [int(x) for x in input().split()]

total = tabela.get(cod, 0) * qt

print(f"Total: R$ {total:.2f}")
