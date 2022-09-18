# -*- coding: utf-8 -*-

a, n = [int(k) for k in input().split() if int(k) > 0]

values = [a + i for i in range(n)]

print(sum(values))
