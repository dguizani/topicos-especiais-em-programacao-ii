# -*- coding: utf-8 -*-

inp = [int(input()), int(input())]
inp.sort()

x, y = inp

values = [str(k) for k in range(x + 1, y) if k % 5 in (2, 3)]

print("\n".join(values))
