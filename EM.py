import networkx as nx
import matplotlib.pyplot as plt


def EM(G):
    return


if __name__ == '__main__':

    G = nx.Graph()
    for i in range(1, 10):
        G.add_node(i)

    G.add_edge(3, 4)
    G.add_edge(1, 3)
    G.add_edge(5, 6)
    G.add_edge(5, 9)
    G.add_edge(7, 8)
    G.add_edge(1, 8)
    G.add_edge(1, 4)
    G.add_edge(8, 5)
    G.add_edge(1, 2)

    nx.draw(G, with_labels=True)
    plt.show()

    EM(G)

'''def search_BP(vet):
    H = nx.MultiGraph()
    for item in range(len(vet) - 1):
        if fabs(vet[item + 1] - vet[item]) > 1:
            H.add_node(vet[item + 1])

    return H


if __name__ == '__main__':
    G = nx.MultiGraph()
    vet = [1, 7, 5, 4, 2, 3, 8, 6]
    G = search_BP(vet)
    nx.draw(G)
    plt.show()'''
