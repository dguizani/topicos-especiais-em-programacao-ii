# -*- coding: utf-8 -*-

    
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculo = "abcdefghijklmnopqrstuvwxyz"

n = int(input())

for _ in range(n):
    string = list(input())

    for i in range(len(string)):
        c = string[i]
        if c in maiusculo + minusculo:
            string[i] = chr(ord(c) + 3)

    string = string[::-1]

    for i in range(len(string) // 2, len(string)):
        string[i] = chr(ord(string[i]) - 1)

    print("".join(string))
