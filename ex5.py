from random import *

def de_pipe():
  
    r = random.random()
    
    if r < 0.10:         # 10 %
        return 1
    elif r < 0.25:       # 15 % (0.10 à 0.25)
        return 2
    elif r < 0.40:       # 15 % (0.25 à 0.40)
        return 3
    elif r < 0.55:       # 15 % (0.40 à 0.55)
        return 4
    elif r < 0.70:       # 15 % (0.55 à 0.70)
        return 5
    else:                # 30 % (0.70 à 1.00)
        return 6

jets = [de_pipe() for _ in range(100)]
print(jets)