from math import fabs, ceil
from itertools import combinations
import time

d = 0
r = []
r2 = []
BP = 0
deltaPhi = []


def gera_Gollan(x):
    gol = []
    for i in range(1, x + 1):
        if i == 1:
            gol.append(1)
        elif len(gol) % 2 == 0:
            gol.insert(len(gol) - 1, i)
        elif len(gol) % 2 != 0:
            gol[len(gol) - 1], gol[len(gol) - 2] = gol[len(gol) - 2], gol[len(gol) - 1]
            gol.insert(len(gol) - 2, i)
    return gol


def clearGlobais():
    global d
    global r
    global r2
    global BP
    global deltaPhi

    d = 0
    r = []
    r2 = []
    BP = 0
    deltaPhi = []


def count_BP(vet):
    global BP
    for item in range(len(vet) - 1):
        if fabs(vet[item + 1] - vet[item]) > 1:
            BP = BP + 1


def reversao(i, j, vet):
    prefix = vet[:i]
    vetRev = vet[i:j + 1][::-1]
    sufix = vet[j + 1:]

    return prefix + vetRev + sufix


def makeDeltaPhi(vet):
    global deltaPhi
    revList = []
    ep1 = ep2 = 0
    x = 0

    vet2 = [i for i in range(1, len(vet) - 1)]

    for cb in combinations(vet2, 2):
        revList.append(list(cb))

    for item in revList:
        # Verifica a qtd  de BP
        qtBP = qtBP2 = 0

        ep1 = fabs(vet[item[0] - 1] - vet[item[0]])
        ep2 = fabs(vet[item[1]] - vet[item[1] + 1])

        if ep1 > 1:
            qtBP += 1
        if ep2 > 1:
            qtBP += 1

        ep1 = fabs(vet[item[0] - 1] - vet[item[1]])
        ep2 = fabs(vet[item[0]] - vet[item[1] + 1])

        if ep1 > 1:
            qtBP2 += 1
        if ep2 > 1:
            qtBP2 += 1

        x = qtBP - qtBP2

        item.append(x)

    deltaPhi = sorted(revList, key=lambda x: x[2], reverse=True)


def UpperBound(vet):
    global d
    global r
    vet2 = vet
    tam = len(vet)
    for i in range(1, tam - 1):
        if vet2[i] != i:
            for j in range(i + 1, tam - 1):
                if vet2[j] == i:
                    vet2 = reversao(i, j, vet2)
                    d = d + 1
                    r.append([i, j])


def LowerBound(vet):
    # qtd BP / 2
    count_BP(vet)
    return ceil(BP / 2)


def Bnb(vet):
    UpperBound(vet)
    search(vet, 0)


def search(vet, d2):
    global d
    global r
    global r2

    if vet == sorted(vet):
        d = d2
        r = r2

    else:
        makeDeltaPhi(vet)
        for item in deltaPhi:
            d3 = d2 + 1
            vet2 = reversao(item[0], item[1], vet)

            if d3 + LowerBound(vet2) < d:
                r2.append([item[0], item[1]])
                search(vet2, d3)


############ MAIN ############
if __name__ == "__main__":

    ### Teste Permutacoes de Gollan ###
    for i in range(1, 5):
        vet = []
        vet = gera_Gollan(i)

        vet.insert(0, 0)
        vet.insert(len(vet), len(vet))

        inicio = time.time()
        Bnb(vet)
        fim = time.time() - inicio

        print(vet, i, fim)

        clearGlobais()
