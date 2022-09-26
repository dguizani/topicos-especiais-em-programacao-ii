# -*- coding: utf-8 -*-

while True:
    n, v = input().split()
    
    if n == v == "0":
        break
    
    try:
        print(int(v.replace(n, "")))
    except:
        print(0)
