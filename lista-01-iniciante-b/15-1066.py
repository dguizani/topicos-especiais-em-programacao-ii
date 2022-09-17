# -*- coding: utf-8 -*-

values = [
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input())
]

qt_par = len([x for x in values if x % 2 == 0])
qt_impar = len([x for x in values if x % 2 != 0])
qt_positivo = len([x for x in values if x > 0])
qt_negativo = len([x for x in values if x < 0])

print(f"{qt_par} valor(es) par(es)")
print(f"{qt_impar} valor(es) impar(es)")
print(f"{qt_positivo} valor(es) positivo(s)")
print(f"{qt_negativo} valor(es) negativo(s)")
