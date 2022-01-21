from generate_flag import generateFlag 
import random

def generateSeededFlag(seed=None, count=3):
    if seed == None:
        seed = ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(6)])
    else:
        seed = seed
    g = generateFlag(count, seed.upper())
    g.run()

generateSeededFlag("cumgender")