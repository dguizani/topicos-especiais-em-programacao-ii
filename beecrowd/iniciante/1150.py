# -*- coding: utf-8 -*-

x = int(input())

while True:
    z = int(input())
    
    if z > x:
        break

count = soma = 0

while soma < z:
    soma += x
    count += 1
    x += 1

print(count)
