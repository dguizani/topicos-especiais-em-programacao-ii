# -*- coding: utf-8 -*-

inp = [int(input()), int(input())]
inp.sort()

x, y = inp

values = [k for k in range(x, y + 1) if k % 13 != 0]

print(sum(values))
