from tkinter import E


# -*- coding: utf-8 -*-

x = int(input())

values = [int(input()) for _ in range(x)]

r = [x for x in range(10, 21)]

v_in = len([x for x in values if x in r])
v_out = len(values) - v_in

print(f"{v_in} in")
print(f"{v_out} out")
