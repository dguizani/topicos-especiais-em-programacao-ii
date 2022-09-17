# -*- coding: utf-8 -*-

v = float(input())

if v <= 2000:
    print("Isento")

else:
    if v <= 3000:
        imp = (v - 2000) * 0.08

    elif v <= 4500:
        imp = ((v - 3000) * 0.18) + 80

    else:
        imp = ((v - 4500) * 0.28) + 350

    print(f"R$ {imp:.2f}")
