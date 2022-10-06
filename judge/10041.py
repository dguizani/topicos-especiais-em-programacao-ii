# -*- coding: utf-8 -*-

"""
O gângster mundialmente conhecido Vito Deadstone está se mudando para Nova York.
Ele tem uma família muito grande lá, todos morando na Avenida Lamafia. Como ele
vai visitar todos os seus parentes com muita frequência, ele está tentando
encontrar uma casa perto deles

Vito quer minimizar a distância total de todos eles e chantageou você para
escrever um programa que resolva o problema dele.

A entrada consiste em vários casos de teste. A primeira linha contém o número de
casos de teste.

Entrada

Para cada caso de teste, você receberá o número inteiro de parentes r (0 < r < 500)
e os números das ruas (também inteiros) s1, s2, ... , si, ... , sr onde moram
(0 < si < 30000 ). Observe que vários parentes podem morar no mesmo número de rua.

Resultado

Para cada caso de teste seu programa deve escrever a soma mínima das distâncias
da casa ótima de Vito a cada um de seus parentes. A distância entre dois números
de rua si e sj é dij = | si - sj |.

Entrada de amostra
2
2 2 4
3 2 4 6

Saída de Amostra
2
4
"""

qtt_casos = int(input())

for _ in range(qtt_casos):
    caso_teste = [int(x) for x in input().split()][1:]
    
    caso_teste.sort()
    
    meio = caso_teste[len(caso_teste) // 2]
    
    print(sum([abs(meio - c) for c in caso_teste]))
