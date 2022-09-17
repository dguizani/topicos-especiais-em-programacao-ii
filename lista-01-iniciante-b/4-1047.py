# -*- coding: utf-8 -*-

import datetime as dt


hi1, mi1, hf2, mf2 = [int(x) for x in input().split()]

h1 = dt.timedelta(hours=hi1, minutes=mi1)
h2 = dt.timedelta(hours=hf2, minutes=mf2)

if h1 == h2:
    h_diff = 24
    m_diff = 0
else:
    s_diff = (h2 - h1).seconds
    h_diff = s_diff // 60 // 60
    
    if h_diff > 0:
        m_diff = (s_diff - h_diff) // 60 // 60
    else:
        m_diff = s_diff // 60

print(f"O JOGO DUROU {h_diff} HORA(S) E {m_diff} MINUTO(S)")
