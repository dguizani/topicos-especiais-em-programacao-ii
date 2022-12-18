# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    e = 0
    
    a = int(n * (n + 1) * (2 * n + 1) / 6)
    b = int((n + 1) * n / 2 * (n + 1) * n / 2 - a)
    c = int(n * (n + 1) / 2 * n * (n + 1) / 2)
    d = int((n + 1) * n / 2 * (n + 1) * n / 2 * (n + 1) * n / 2 - c)

    for i in range(1, n + 1):
        e += i ** 4

    f = int((n + 1) * n / 2 * (n + 1) * n / 2 * (n + 1) * n / 2 * (n + 1) * n / 2 - e)

    print(a, b, c, d, e, f)
