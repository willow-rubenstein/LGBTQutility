# LGBTQutility v1 by Ashe Muller!

## What is this???
- This is just a small side-project I made while waiting for the 
rest of the materials for my next osu! video to arrive
- I have done this project a few times before in the past, but I
wanted to redo it again, and make it open-source this time

## How to use?
- Usage is really simple:
- Use Python 3x
- `pip install -r requirements.txt`
> Inside of your program you are using this with, take the original script, and
> Integrate it as such in a seperate file in the same directory:
```
from generate_flag import generateFlag 
import random

def generateSeededFlag(seed=None, count=3):
    if seed == None:
        seed = ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(6)])
    else:
        seed = seed
    g = generateFlag(count, seed.upper())
    g.run()
```
> Run generateSeededFlag with the arguments to create a flag of your very own!
> Or, just modify tests.py to your liking!
