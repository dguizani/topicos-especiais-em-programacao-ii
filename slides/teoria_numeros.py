"""
    Qual o último digito de x^y?
"""

from random import randint


x = randint(0, 100)
y = randint(0, 100)

mod_y = 4

if y == 0:
    num = 1

elif y % mod_y == 0:
    num = x ** mod_y

else:
    num = x ** (y % mod_y)

print(f"O último digito de {x} ** {y} = {num % 10}")
print(f"O último digito de {x} ** {y} = {(x ** y) % 10}")
