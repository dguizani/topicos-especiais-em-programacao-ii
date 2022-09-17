# -*- coding: utf-8 -*-

import datetime as dt


h1, h2 = [dt.timedelta(hours=int(x)) for x in input().split()]

if h1 == h2:
    h_diff = 24
else:
    h_diff = (h2 - h1).seconds // 60 // 60

print(f"O JOGO DUROU {h_diff} HORA(S)")
