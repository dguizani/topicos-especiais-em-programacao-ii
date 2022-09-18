# -*- coding: utf-8 -*-

alcool = 0
gasolina = 0
diesel = 0


def inc_alcool():
    globals()["alcool"] = globals()["alcool"] + 1


def inc_gasolina():
    globals()["gasolina"] = globals()["gasolina"] + 1


def inc_diesel():
    globals()["diesel"] = globals()["diesel"] + 1


def sair():
    return True


options = {
    1: inc_alcool,
    2: inc_gasolina,
    3: inc_diesel,
    4: sair
}


while True:
    inc = options.get(int(input()))

    if inc is None:
        continue
    
    if inc():
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
