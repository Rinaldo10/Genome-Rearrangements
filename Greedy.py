from math import fabs #funcao absoluta
import random

##-------------------------------------------##
##-------------Variaveis globais-------------##
##-------------------------------------------##

vetI = []  # Inversa da permutacao
BP = 0  # Qtd de Breakpoints
down = []  # Informacoes das strips
d = 0  # Qtd de passos para ordenar permutacao
lista = []  # Lista das reversoes feitas


##-------------------------------------------##
##---Limpa as Globais p/ multiplos testes----##
##-------------------------------------------##

def clearGlobais():
    global vetI
    global down
    global lista
    global BP
    global d
    vetI = []
    down = []
    lista = []
    BP = 0
    d = 0


##------------------------------------------------------------------------------##
## makeDown(vet): recebe um vetor de números inteiros "vet" (permutacao) e devolve
## o vetor "down", que contém informações das strips decrescentes.
##-----------------------------------------------------------------##

def makeDown(vet):
    global down
    down = []
    key = 0
    for i in range(1, len(vet) - 1):
        if i == 1 or i == len(vet) - 2:
            down.append(key)
        elif vet[i] > vet[i - 1]:
            key += 1
            down.append(key)
        else:
            down.append(key)

    down.insert(0, 0)
    down.insert(len(vet), 0)

    return


##-------------------------------------------------------------------##
## inversa(vet): recebe um vetor de números inteiros "vet" e devolve
## o vetor "vetI", que contém a inversa da permutação contida em vet
##-------------------------------------------------------------------##

def inversa(vet):
    global vetI
    vetI = [0] * len(vet)
    for i in range(len(vet)):
        vetI[vet[i]] = i


##---------------------------------------------------------------------##
## countBP(vet): recebe um vetor de números inteiros "vet" e devolve
## a variavel "BP", que contém a quantidade de breakpoints da permutacao
##---------------------------------------------------------------------##

def countBP(vet):
    global BP
    BP = 0
    for i in range(len(vet) - 1):
        if fabs(vet[i + 1] - vet[i]) > 1:
            BP += 1


##---------------------------------------------------------------------##
## reversao(i, j, vet): recebe um intervalo [i,j] endpoints e um vetor
## de números inteiros "vet", e devolve o vetor prefix+vetRev+sufix, que
##contém a nova permutação com o intervalo [i, j] revertido.
##---------------------------------------------------------------------##

def reversao(i, j, vet):
    prefix = vet[:i]
    vetRev = vet[i:j + 1][::-1]
    sufix = vet[j + 1:]

    return prefix + vetRev + sufix


##-------------------------------------------------------------------------##
## searchCandidate(vet): recebe um vetor de números inteiros "vet" e devolve
## a melhor reversao possível a ser feita, retornando o intervalo "candidate[i, j]"
## seja ela uma 2-reversão, 1-reversão (com strip decrescente), 1-reversao ou
## uma 0-reversao
##-------------------------------------------------------------------------##

def searchCandidate(vet):
    pivo = 0
    candidate = []
    # busca 2-reversao
    for i in range(1, len(vet) - 2):
        if pivo != 2:
            if fabs(vet[i] - vet[i - 1]) > 1:
                A = vetI[vet[i] + 1]
                B = vetI[vet[i] - 1]

                # verifica se remove o BP [i, i-1] com A
                if fabs(vet[i - 1] - vet[A - 1]) == 1 and fabs(vet[A] - vet[A - 1]) > 1 and A > i:
                    pivo = 2
                    candidate.append(i)
                    candidate.append(A - 1)

                # verifica se remove o BP [i, i-1] com B
                elif fabs(vet[i - 1] - vet[B - 1]) == 1 and fabs(vet[B] - vet[B - 1]) > 1 and B > i:
                    pivo = 2
                    candidate.append(i)
                    candidate.append(B - 1)

        # busca 1-reversao SD
        if pivo == 0:
            for i in range(1, len(vet) - 1):
                if pivo != 1:
                    if fabs(vet[i] - vet[i - 1]) > 1:
                        A = vetI[vet[i] + 1]
                        B = vetI[vet[i] - 1]

                        # IFs verificam se é possivel remover 1 BP, analisando o formato da permutacao e da strip

                        if fabs(i - A) == 1 and fabs(vet[A] - vet[i - 1] == 1) and fabs(down[i] - down[A]) > 0:
                            candidate.append(i)
                            candidate.append(A)
                            pivo = 1

                        if pivo != 1 and fabs(vet[A] - vet[A - 1]) > 1 and fabs(down[i] - down[A]) > 0:
                            candidate.append(i)
                            candidate.append(A - 1)
                            pivo = 1

                        if pivo != 1 and fabs(i - B) == 1 and fabs(vet[B] - vet[i - 1] == 1) and fabs(
                                down[i] - down[B]) > 0:
                            candidate.append(i)
                            candidate.append(B)
                            pivo = 1

                        if pivo != 1 and fabs(vet[B] - vet[B - 1]) > 1 and B > i and fabs(down[i] - down[B]) > 0:
                            candidate.append(i)
                            candidate.append(B - 1)
                            pivo = 1

    # busca 1-reversao
    if pivo == 0:
        for i in range(1, len(vet) - 1):
            if pivo != 1:
                if fabs(vet[i] - vet[i - 1]) > 1:
                    A = vetI[vet[i] + 1]
                    B = vetI[vet[i] - 1]

                    # IFs verificam se é possivel remover 1 BP, analisando o formato da permutacao

                    if fabs(i - A) == 1 and fabs(vet[A] - vet[i - 1] == 1):
                        candidate.append(i)
                        candidate.append(A)
                        pivo = 1

                    if pivo != 1 and fabs(vet[A] - vet[A - 1]) > 1:
                        candidate.append(i)
                        candidate.append(A - 1)
                        pivo = 1

                    if pivo != 1 and fabs(i - B) == 1 and fabs(vet[B] - vet[i - 1] == 1):
                        candidate.append(i)
                        candidate.append(B)
                        pivo = 1

                    if pivo != 1 and fabs(vet[B] - vet[B - 1]) > 1 and B > i:
                        candidate.append(i)
                        candidate.append(B - 1)
                        pivo = 1

    # executa 0-reversão
    if pivo == 0:
        for i in range(0, len(vet) - 2):
            if pivo != 1:
                if fabs(vet[i] - vet[i + 1]) > 1:
                    A = vetI[vet[i] + 1]

                    if i < A:
                        candidate.append(i + 1)
                        candidate.append(A)
                        pivo = 1

                    elif i > A:
                        candidate.append(A + 1)
                        candidate.append(i)
                        pivo = 1
        pivo = 0

    # candidate.append(pivo)
    return candidate


##----------------------------------------------------------------------------------------##
## greedy(vet): recebe um vetor de números inteiros "vet", itera sobre a quantidade
## de breakpoints, atualizando as variaveis globais a cada iteração, aplicando as reversoes
## e devolvendo o vetor (permutação) "vet" ordenado.##
##----------------------------------------------------------------------------------------##

def greedy(vet):
    global BP
    global lista
    global d

    countBP(vet)

    while BP > 0:
        inversa(vet)
        makeDown(vet)
        cand = searchCandidate(vet)
        vet = reversao(cand[0], cand[1], vet)
        lista.append([cand[0], cand[1]])
        d += 1
        countBP(vet)

    print("Ordenado:", vet == sorted(vet))


##-----------------------------------------------------------##
## Main: cria o vetor "vet" (permutação) e executa
## multiplos testes. Retorna a quantidade de passos necessária
## para ordenar a permutação e as reversões feitas para isso.
##-----------------------------------------------------------##

if __name__ == '__main__':
    # teste com 10 permutaçoes randomicas de 10 elementos
    for i in range(10):
        vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # permutacao
        random.shuffle(vet)  # randomiza permutacao
        vet.insert(0, 0)
        vet.insert(len(vet), len(vet))
        greedy(vet)
        print("Passos:", d)
        print("Reversoes:", lista)
        clearGlobais()
