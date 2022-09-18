# -*- coding: utf-8 -*-

values = [int(input()) for _ in range(100)]

maior = max(values)

print(maior)
print(values.index(maior) + 1)
