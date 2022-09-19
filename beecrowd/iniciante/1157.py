# -*- coding: utf-8 -*-

n = int(input())

values = [str(i) for i in range(1, n + 1) if n % i == 0]

print("\n".join(values))
