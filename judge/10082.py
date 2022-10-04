# -*- coding: utf-8 -*-

keys = list("`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./")

while True:
    string = list(input())
    
    if not string:
        break
    
    for i in range(len(string)):
        j = 0
        while True:
            if string[i] in " \n":
                break
            elif string[i] == keys[j]:
                string[i] = keys[j - 1]
                break
            j += 1
    
    print("".join(string))
