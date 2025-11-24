from random import *
def simulation_des_lancers(nb_lancers: int = 100):
    resultats = []
    for _ in range(nb_lancers):
        lancer = random.randint(1, 6)
        resultats.append(lancer)
    return resultats
