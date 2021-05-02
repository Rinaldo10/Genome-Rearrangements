import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx import bipartite

from math import fabs  # funcao absoluta

vetI = []  # Inversa


def clearGlobais():
    global vetI
    vetI = []


def makeEdges(G, vet):
    for i in range(1, len(vet) - 1):

        if fabs(vet[i] - vet[i - 1]) > 1:

            A = vetI[vet[i] + 1]
            B = vetI[vet[i] - 1]

            # verifica se remove o BP [i, i-1] com A

            if fabs(vet[i - 1] - vet[A - 1]) == 1 and fabs(vet[A] - vet[A - 1]) > 1 and fabs(i - A) > 1 and A > i:
                G.add_edge(i, A)

            # verifica se remove o BP [i, i-1] com B
            elif fabs(vet[i - 1] - vet[B - 1]) == 1 and fabs(vet[B] - vet[B - 1]) > 1 and fabs(i - B) > 1 and B > i:
                G.add_edge(i, B)

            elif A < len(vet) - 1 and fabs(vet[i - 1] - vet[A + 1]) == 1 and fabs(vet[A] - vet[A + 1]) > 1 and fabs(
                    i - A) > 1:
                G.add_edge(i, A + 1)

            elif fabs(vet[i - 1] - vet[B + 1]) == 1 and fabs(vet[B] - vet[B + 1]) > 1 and B > i and fabs(i - B) > 1:
                G.add_edge(i, B + 1)

    return G


def inversa(vet):
    global vetI
    vetI = [0] * len(vet)
    for i in range(len(vet)):
        vetI[vet[i]] = i

    return vetI


def makeNodes(vet):
    H = nx.MultiGraph()
    for i in range(1, len(vet)):
        if fabs(vet[i] - vet[i - 1]) > 1:
            H.add_node(i)

    return H


def extern(vet):
    inversa(vet)
    G = makeNodes(vet)
    G = makeEdges(G, vet)
    return nx.maximal_matching(G)


if __name__ == '__main__':
    mm = 0
    G = nx.MultiGraph()
    vet = [0, 4, 7, 1, 5, 3, 6, 2, 8, 9]
    inversa(vet)
    G = makeNodes(vet)
    G = makeEdges(G, vet)

    for c in nx.connected_components(G):
        S = G.subgraph(c).copy()
        print(len(nx.bipartite.hopcroft_karp_matching(S))/2)

    nx.draw(G, with_labels=True)
    plt.show()

    '''for i in range(10):
        G = nx.MultiGraph()
        vet = [1, 7, 5, 4, 2, 3, 8, 6]
        random.shuffle(vet)
        vet.insert(0, 0)
        vet.insert(len(vet), len(vet))
        print(vet)
        inversa(vet)
        G = makeNodes(vet)
        G = makeEdges(G, vet)

        print(nx.bipartite.sets(G))

        nx.draw(G, with_labels=True)
        plt.show()
        clearGlobais()'''
