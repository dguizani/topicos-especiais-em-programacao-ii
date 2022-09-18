# -*- coding: utf-8 -*-

def sair():
    while True:
        sair = int(input("Novo grenal (1-sim 2-nao)\n"))
        
        if sair not in (1, 2):
            continue
        
        return sair == 2


qt_grenais = 0
vi_inter = 0
vi_gremio = 0
empates = 0

while True:
    gols_inter, gols_gremio = [int(k) for k in input().split()]
    
    qt_grenais += 1
    
    if gols_inter == gols_gremio:
        empates += 1
    elif gols_inter > gols_gremio:
        vi_inter += 1
    else:
        vi_gremio += 1
    
    if sair():
        break

print(f"{qt_grenais} grenais")
print(f"Inter:{vi_inter}")
print(f"Gremio:{vi_gremio}")
print(f"Empates:{empates}")

if vi_inter == vi_gremio:
    print("Nao houve vencedor")
elif vi_inter > vi_gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
