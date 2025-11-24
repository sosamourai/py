from random import *

def lancer_trois_des():

    de1 = random.randint(1, 6)   # premier dé
    de2 = random.randint(1, 6)   # deuxième dé
    de3 = random.randint(1, 6)   # troisième dé
    
    somme = de1 + de2 + de3
    return de1, de2, de3, somme


d1, d2, d3, total = lancer_trois_des()