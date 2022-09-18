# -*- coding: utf-8 -*-

import datetime as dt


hi1, mi1, hf2, mf2 = [int(x) for x in input().split()]

h1 = dt.timedelta(hours=hi1, minutes=mi1)
h2 = dt.timedelta(hours=hf2, minutes=mf2)

if h1 == h2:
    h_diff = 24
    m_diff = 0
else:
    m_diff, segundo = divmod((h2 - h1).seconds, 60)
    h_diff, m_diff = divmod(m_diff, 60)

print(f"O JOGO DUROU {h_diff} HORA(S) E {m_diff} MINUTO(S)")
