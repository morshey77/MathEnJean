import matplotlib.pyplot as plt

def makeGraphic(tab:dict) -> None:
    plt.plot(tab.keys(), tab.values())
    plt.xlabel('Nème branche')
    plt.ylabel('Nombre de ruine')
    plt.savefig('./result/graphic.png')