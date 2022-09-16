# -*- coding: utf-8 -*-

N1, N2, N3, N4 = [float(x) for x in input().split()]

P1, P2, P3, P4 = [2, 3, 4, 1]

s_peso = P1 + P2 + P3 + P4

media = ((N1 * P1) + (N2 * P2) + (N3 * P3) + (N4 * P4)) / s_peso

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    N5 = float(input())
    
    print(f"Nota do exame: {N5}")
    
    media = (media + N5) / 2
    
    if media >= 4:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media}")
