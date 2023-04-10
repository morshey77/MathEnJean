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

# Method use to make this
from excel import makeExcel
from graphic import makeGraphic
from randomgraph import randomGraph

# Gain and loss amounts
GAIN, LOSS, TAB = 2, 1, {}

# Recursive function to check all probabilities
async def check(columns:int, row:int, euro:int, step:int = 0) -> None:
    if euro == row:
        # Update probabilities in TAB
        if row not in TAB:
            TAB[row] = {i: 0 for i in range(columns + 1)}
        TAB[row][step] += 1

    # Check for valid steps and euro values
    if euro > 0 and step < columns:
        # Check gain and loss scenarios
        await check(columns, row, euro + GAIN, step + 1)
        await check(columns, row, euro - LOSS, step + 1)

# Prompt user for number of columns and rows
columns, rows = min(int(input('Nombre de colonne (Branche - Maximun 20) : ')), 20), min(int(input('Nombre de ligne (Somme Euro - Maximun 20) : ')), 20)

# Prompt user for initial sum
sum = int(input('Somme initial : '))

# Print message to indicate data loading
print('Chargement des données...')

# Record start time
start_time = time.time()

# Launch probability calculations
for row in range(rows + 1):
    asyncio.run(check(columns, row, sum))

# Transform TAB to excel file's
makeExcel(TAB, columns)

makeGraphic(TAB[0])

randomGraph()

# Print elapsed time
elapsed_time = time.time() - start_time
print(f"Données chargées en {(elapsed_time):.2f} secondes.")