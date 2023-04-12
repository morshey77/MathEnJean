import matplotlib.pyplot as plt

from random import getrandbits

def makeGraphic(tab:dict) -> None:

    plt.plot(tab.keys(), tab.values())
    plt.title('Simulation du nombre de ruines à chaque tour (branche)')
    plt.xlabel('Nème branche')
    plt.ylabel('Nombre de ruine')
    plt.savefig('./result/graphic.png')

    # Remove last plot
    plt.clf()

    l, n, e = int(input("Longueur : ")), 2, 15
    tab = {i: [] for i in range(e)}

    for i in range(e):
        v = n
        for _ in range(l):
            # 3 * [0, 1] - 1 = [2 Win, -1 Lose]
            tab[i].append((v := v + 3*getrandbits(1) - 1))

    for h in tab.keys():
        plt.plot(range(l), tab[h])
        print(max(tab[h]))

    plt.title('Simulation du solde de plusieurs personnes \n qui joue à chaque tour (branche)')
    plt.xlabel('Nème branche')
    plt.ylabel("Nombre d'euro")
    plt.savefig('./result/randomGraph.png')