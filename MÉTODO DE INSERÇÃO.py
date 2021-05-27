# COLOCA O VETOR EM ORDEM CRESCENTE PELO MÉTODO DE INSERÇÃO

import random

def criaVetor(n):
    vetor = [0] * n
    for i in range(n):
        vetor[i] = random.randint(0, 30)
    return vetor

def insert(vetor):
    for k in range(1, len(vetor)):
        x = vetor[k]
        i = k
        while i > 0 and x < vetor[i - 1]:
            vetor[i] = vetor[i - 1]
            i -= 1
            vetor[i] = x
    return vetor

def main():
    n = 5
    vetor = criaVetor(n)
    print(insert(vetor))

main()