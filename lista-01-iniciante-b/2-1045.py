# -*- coding: utf-8 -*-

lados = [float(x) for x in input().split()]

lados.sort(reverse=True)

a, b, c = lados

a_2 = a ** 2

b_2_c_2 = (b ** 2) + (c ** 2)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a_2 == b_2_c_2:
        print("TRIANGULO RETANGULO")

    if a_2 > b_2_c_2:
        print("TRIANGULO OBTUSANGULO")

    if a_2 < b_2_c_2:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")

    if a == b and a != c:
        print("TRIANGULO ISOSCELES")

    if a == c and a != b:
        print("TRIANGULO ISOSCELES")

    if c == b and c != a:
        print("TRIANGULO ISOSCELES")
