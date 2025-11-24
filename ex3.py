from random import *

def simulation_trois_des(nb_jets: int = 50):

    resultats = []
    for _ in range(nb_jets):
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        de3 = random.randint(1, 6)
        somme = de1 + de2 + de3
        resultats.append((de1, de2, de3, somme))
    return resultats

# Programme principal
jets = simulation_trois_des(50)

# Affichage des 10 premiers résultats pour vérifier
for i in range(10):
    print(f"Jet {i+1} : Dé1 = {jets[i][0]}, Dé2 = {jets[i][1]}, Dé3 = {jets[i][2]}, Somme = {jets[i][3]}")
