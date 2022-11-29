# -*- coding: utf-8 -*-

"""
Luiz é um coordenador muito dedicado do curso de ciência da computação. Ele sabe
a importância de incentivar seus alunos a esforçarem-se em algoritmos, por isso
decidiu realizar uma competição de programação individual entre estes, com direito
a premiação.

Luiz gostaria de evitar ao máximo a possibilidade de fraude na competição, e por
isso não gostaria que houvessem dois candidatos amigos na mesma sala durante a
realização da prova.

Infelizmente Luiz só dispõe de duas salas para a realização da prova, mas felizmente
conhece muito bem seus alunos, e sabe dizer com facilidade quem é amigo de quem.
Entretanto, ele precisa saber se será possível, apenas com as duas salas disponíveis,
combinar os alunos da forma que deseja e para isso solicitou a você, aluno dedicado
do curso, que crie um programa para ajudá-lo.

Entrada
A entrada é composta de diversos casos de teste. A primeira linha de cada caso de
teste consiste em um inteiro N (2 ≤ N ≤ 100) indicando o número de alunos que irão
realizar a prova.

Cada N par de linhas seguintes descreve as relações de amizade de cada participante,
de forma que a primeira linha consiste no identificador do participante, e a linha
seguinte consiste em uma lista descrevendo uma quantidade M de alunos (1 ≤ M < N) com
os quais aquele participante possui uma relação de amizade.

Considere que não é relevante o número de pessoas dispostas em cada sala, e que,
se existe uma relação de amizade entre alunos x e y, existe uma relação de amizade
entre y e x. A entrada termina quando N = 0, e não deve ser processada.

Saída
Para cada caso de teste, deverá ser impressa uma linha contendo a resposta "SIM",
caso seja possível dispor os alunos de forma que não hajam dois amigos realizando
a prova na mesma sala, e "NAO", caso contrário.
"""

class Grafo:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.mat_adjacencia = [[0] * vertices for _ in range(vertices)]

    def add_aresta(self, vertice_x: int, vertice_y: int):
        self.mat_adjacencia[vertice_x - 1][vertice_y - 1] += 1

    def validar(self):
        *a, = [tuple(x) for x in self.mat_adjacencia]
        *t, = zip(*self.mat_adjacencia)
        
        return a == t

    def __str__(self) -> str:
        str_ = ""
        
        for linha in self.mat_adjacencia:
            str_ += str(linha) + "\n"

        return str_

    def __repr__(self) -> str:
        return str(self)


while (n := int(input())) != 0:
    grafo = Grafo(n)
    
    for _ in range(n):
        p = int(input())
        relacoes = [int(x) for x in input().split()]
        
        for r in relacoes:
            grafo.add_aresta(p, r)

    if grafo.validar():
        print("SIM")

    else:
        print("NÃO")
