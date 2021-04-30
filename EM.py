import networkx as nx
import matplotlib.pyplot as plt
from math import fabs  # funcao absoluta

vetI = []  # Inversa


def makeEdges(G, vet):
    global vetI
    for i in range(1, len(vet) - 1):
        if fabs(vet[i] - vet[i - 1]) > 1:
            print(vetI)
            A = vetI[vet[i] + 1]
            B = vetI[vet[i] - 1]

            # verifica se remove o BP [i, i-1] com A
            print(i)
            if fabs(vet[i - 1] - vet[A - 1]) == 1 and fabs(vet[A] - vet[A - 1]) > 1 and A > i:
                G.add_edge(i, A)

            # verifica se remove o BP [i, i-1] com B
            elif fabs(vet[i - 1] - vet[B - 1]) == 1 and fabs(vet[B] - vet[B - 1]) > 1 and B > i:
                G.add_edge(i, B)

            elif A < len(vet)-1 and fabs(vet[i - 1] - vet[A + 1]) == 1 and fabs(vet[A] - vet[A + 1]) > 1:
                G.add_edge(i, A)

            elif fabs(vet[i - 1] - vet[B + 1]) == 1 and fabs(vet[B] - vet[B + 1]) > 1 and B > i:
                G.add_edge(i, B)

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


if __name__ == '__main__':
    G = nx.MultiGraph()
    vet = [0, 1, 7, 5, 4, 2, 3, 8, 6, 9]
    inversa(vet)
    G = makeNodes(vet)
    G = makeEdges(G, vet)

    nx.draw(G, with_labels=True)
    plt.show()
