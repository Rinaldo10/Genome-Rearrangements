from math import fabs
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


##--------------------------------------------------##
##--Cria Vetor Down (Contém informaçõs das Strips)--##
##--------------------------------------------------##

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


##--------------------------------------------------##
##--Método que retorna a inversa de uma permutação--##
##--------------------------------------------------##

def inversa(vet):
    global vetI
    vetI = [0] * len(vet)
    for i in range(len(vet)):
        vetI[vet[i]] = i


##--------------------------------------------------##
##----------Método que conta Breakpoints------------##
##--------------------------------------------------##

def countBP(vet):
    global BP
    BP = 0
    for i in range(len(vet) - 1):
        if fabs(vet[i + 1] - vet[i]) > 1:
            BP += 1


##--------------------------------------------------##
##----------Método que faz uma reversao-------------##
##--------------------------------------------------##

def reversao(i, j, vet):
    prefix = vet[:i]
    vetRev = vet[i:j + 1][::-1]
    sufix = vet[j + 1:]

    return prefix + vetRev + sufix


##--------------------------------------------------##
##-------Busca o candidato a melhor reversao--------##
##--------------------------------------------------##

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


##--------------------------------------------------##
##----------------------Main------------------------##
##--------------------------------------------------##

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
