from random import *

def simulation_deux_des(nb_jets: int = 200):
    resultats = []
    for _ in range(nb_jets):
        de1 = random.randint(1, 8)   
        de2 = random.randint(1, 8)   
        somme = de1 + de2 #concatenation d'element obtenus au "hasard"
        resultats.append((de1, de2, somme))
    return resultats

jets = simulation_deux_des(200)


for i in range(10):
    print(f"Jet {i+1} : Dé1 = {jets[i][0]}, Dé2 = {jets[i][1]}, Somme = {jets[i][2]}")