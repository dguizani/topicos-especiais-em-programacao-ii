"""
    Gustavo sabe contar, mas agora está aprendendo a escrever números.
    Como ele é um aluno muito bom, ele já aprendeu 1, 2, 3 e 4. Mas ele
    ainda não percebeu que 4 é diferente de 1, então ele acha que 4 é
    outra forma de escrever 1. Além disso, ele está divertindo com um
    joguinho que ele mesmo criou: ele faz números (com aqueles quatro
    dígitos) e soma seus valores. Por exemplo:
    
    132 = 1 + 3 + 2 = 6
    112314 = 1 + 1 + 2 + 3 + 1 + 1 = 9 (lembre-se que Gustavo pensa que 4 = 1)
    
    Depois de fazer muitos números dessa forma, Gustavo agora quer saber
    quantos números ele pode criar de tal forma que sua soma seja um número
    n. Por exemplo, para n = 2 ele percebeu que pode fazer 5 números: 11,
    14, 41, 44 e 2 (ele sabe contá-los, mas não sabe escrever cinco). No
    entanto, ele não consegue descobrir para n maior que 2. Então, ele pediu
    para você ajudá-lo.
    
    Entrada
    A entrada consistirá em um número arbitrário de conjuntos. Cada conjunto
    consistirá em um inteiro n tal que 1 ≤ n ≤ 1000. Você deve ler até chegar
    ao final do arquivo.
    
    Resultado
    Para cada número lido, você deve emitir outro número (em uma linha sozinha)
    informando quantos números Gustavo pode fazer para que a soma de seus dígitos
    seja igual ao número fornecido.
    
    Sample Input
    2
    3
    
    Sample Output
    5
    13
"""

sol_space = {}

def foo(n):
    global sol_space

    if n < 1:
        return 1

    if n in sol_space:
        return sol_space[n]
    
    sol = 0
    
    if n >= 1:
        sol += 2 * foo(n - 1) 
    if n >= 2:
        sol += foo(n - 2)
    if n >= 3:
        sol += foo(n - 3)
    
    sol_space[n] = sol
    return sol

with open("teste.txt", "w") as f:
    for i in range(1, 1001):
        f.write(f"{foo(i)}\n")

# while True:
#     try:
#         number = int(input())
#         print(foo(number))
#     except EOFError:
#         break
