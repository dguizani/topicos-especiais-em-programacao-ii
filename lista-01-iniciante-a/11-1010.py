# -*- coding: utf-8 -*-

c1, n1, vu1 = input().split()
c2, n2, vu2 = input().split()

v1 = int(n1) * float(vu1)
v2 = int(n2) * float(vu2)

tot_pagar = v1 + v2

print(f"VALOR A PAGAR: R$ {tot_pagar:.2f}")
