# -*- coding: utf-8 -*-

sal = float(input())

if sal <= 400:
    novo_sal = sal + sal * 0.15
    percent = 15

elif sal <= 800:
    novo_sal = sal + sal * 0.12
    percent = 12

elif sal <= 1200:
    novo_sal = sal + sal * 0.10
    percent = 10

elif sal <= 2000:
    novo_sal = sal + sal * 0.07
    percent = 7

else:
    novo_sal = sal + sal * 0.04
    percent = 4

reajuste = novo_sal - sal

print(f"Novo salario: {novo_sal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percent} %")
