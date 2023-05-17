#!/usr/bin/env python.

"""
Ce programme en Python permet de calculer la probabilité de différents scénarios dans un jeu de hasard. 

Il demande d'abord le nombre de colonnes et de lignes à utiliser (dans les limites de 20 colonnes et 20 lignes), 
ainsi que la somme initiale. 

Il utilise ensuite une fonction récursive pour vérifier toutes les probabilités possibles 
et enregistre les résultats dans un dictionnaire. 

Ces résultats sont ensuite enregistrés dans un fichier Excel, ce qui permet de les visualiser facilement. 

Enfin, le programme affiche un message indiquant le temps qu'il a pris pour charger les données.
"""

# Module Python
import asyncio, time, math

# Importation des fonctions nécéssaire à l'affichage
from excel import makeExcel
from graphic import makeGraphic

# Valeur du gain, perte ainsi que la tableau de valeur
GAIN, LOSS, TAB = 2, 1, {}

# Fonction recursive pour enregister tout les branches
async def check(columns:int, row:int, euro:int, step:int = 0) -> None:
    if euro == row:
        # Mise à jour du nombre de branche dans le tableau de valeur
        if row not in TAB:
            TAB[row] = {i: 0 for i in range(columns + 1)}
        TAB[row][step] += 1

    # Vérifie si il na va pas trop long ou si l'on est pas ruiné
    if euro > 0 and step < columns:
        # Vérifie les scénarios gagnant et perdant
        await check(columns, row, euro + GAIN, step + 1)
        await check(columns, row, euro - LOSS, step + 1)

# Demander à l'utilisateur le nombre de colonnes et de lignes
columns, rows = min(int(input('Nombre de colonne (Branche - Maximun 20) : ')), 20), min(int(input('Nombre de ligne (Somme Euro - Maximun 20) : ')), 20)

# Demander à l'utilisateur la somme initiale
sum = int(input('Somme initial : '))

# Afficher un message pour indiquer le chargement des données
print('Chargement des données...')

# Enregistrer l'heure de début
start_time = time.time()

# Lancement des calculs de branche
for row in range(rows + 1):
    asyncio.run(check(columns, row, sum))

# Transforme le tableau de valeur en fichier excel
makeExcel(TAB, columns)
# Transforme les ruines du tableau de valeur en un graphique
makeGraphic(TAB[0])

# Afficher le temps écoulé
elapsed_time = time.time() - start_time
print(f"Données chargées en {(elapsed_time):.2f} secondes.")
