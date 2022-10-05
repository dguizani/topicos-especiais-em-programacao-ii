# -*- coding: utf-8 -*-

"""
    Rihanna tem uma academia de dança e vai participar de uma competição.
    Como todos seus alunos desejam ser seu parceiro, ela resolveu escolher quem
    tem as medidas ideais. Assim:
    
    - O primeiro critério será a altura: o mais próximo de 180 cm.
    - O segundo critério será o peso: o mais próximo de 75kg, sem ultrapassar.
    - O terceiro critério será a ordem crescente do sobrenome da pessoa.
    
    Entradas:
    - Nome (sempre primeiro e último) Altura (sempre cm) Peso (sempre kg).
    
    Saídas:
    - Lista com todos os classificados, ordenados pelos critérios de escolha.
    
    Exemplo de entrada:
    George Bush   195   110
    Harry Truman   180   75
    Bill Clinton   180   75
    Jhon Kennedy   180   65
    Ronald Reagan   165   110
    Richard Nixon   170   70
    Jimmy Carter   180   77
    
    Exemplo de saída:
    Clinton, Bill
    Truman, Harry
    Kennedy, Jhon
    Carter, Jimmy
    Nixon, Richard
    Bush, George
    Reagan, Ronald
"""

class Pessoa():
    def __init__(self, nome, altura, peso) -> None:
        nome_compelo = nome.split()
        
        self.nome = nome_compelo[0]
        self.sobrenome = nome_compelo[1]
        self.altura = int(altura)
        self.peso = int(peso)
    
    def __str__(self) -> str:
        return f"{self.nome}, {self.sobrenome}"
    
    def __repr__(self) -> str:
        return str(self)
    
    # menor que
    def __lt__(self, __o: object) -> bool:
        altura_base = 180
        peso_base = 75
        
        _abs_1 = abs(altura_base - self.altura)
        _abs_2 = abs(altura_base - __o.altura)
        
        if _abs_1 < _abs_2:
            return True
        
        if _abs_1 == _abs_2:
            if self.peso > peso_base and __o.peso <= peso_base:
                return False
            
            if self.peso == __o.peso:
                return self.sobrenome < __o.sobrenome
            
            if __o.peso > peso_base:
                return True
        
        return False


lista_pessoas = []

while True:
    try:
        pessoa = Pessoa(*input().split("   "))
        lista_pessoas.append(pessoa)
    except:
        break

lista_pessoas.sort()

for p in lista_pessoas:
    print(p)
