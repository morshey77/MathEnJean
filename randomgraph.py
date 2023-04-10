import matplotlib.pyplot as plt
from random import getrandbits

def randomGraph():

    l, n, e = int(input("Longueur : ")), 2, 15
    tab = {i: [] for i in range(e)}

    for i in range(e):
        v = n
        for _ in range(l):
            # 3 * [0, 1] - 1 = [2 Win, -1 Lose]
            tab[i].append((v := v + 3*getrandbits(1) - 1))
    
    # Remove last plot (graphic.py)
    plt.clf()

    for h in tab.keys():
        plt.plot(range(l), tab[h])
        print(max(tab[h]))

    plt.xlabel('Nème branche')
    plt.ylabel("Nombre d'euro")
    plt.savefig('./result/randomGraph.png')
