# -*- coding: utf-8 -*-

valores = [int(x) for x in input().split()]

in_order = [x for x in valores]
in_order.sort()

print("\n".join([str(x) for x in in_order]), end="\n\n")
print("\n".join([str(x) for x in valores]))
