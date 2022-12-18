# -*- coding: utf-8 -*-

def sort(list_: list):
    list_.sort(reverse=True)
    
    return list_


while True:
    try:
        l, c, r1, r2 = [int(x) for x in input().split()]
    except:
        break
    
    if l == c == r1 == r2 == 0:
        break

    r = r1 + r2

    l, c = sort([l, c])
    r1, r2 = sort([r1, r2])
    
    coef = (l - r) ** 2 + (c - r) ** 2
    
    if (c >= 2 * r1) and (coef >= r ** 2):
        print("S")
    else:
        print("N")
