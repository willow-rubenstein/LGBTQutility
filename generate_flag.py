from PIL import Image, ImageDraw
import itertools
import random

class generateFlag:
    def __init__(self, count, seed):
        self.seed = seed
        self.flag = Image.new("RGB", (3840, 2160), "white")
        self.draw = ImageDraw.Draw(self.flag)
        self.last_position = 0
        self.count = count
        self.color = open('colors.txt', 'r').read().split('\n')
        random.seed(self.seed)
        self.colors = [random.choice(self.color) for i in range(count)]
        print(f"Got colors for flag: {self.colors} using seed {self.seed}")
    
    def createStripes(self):
        for i in range(self.count+1):
            y_position = round(2160/self.count*i)
            color = self.colors[i-1]
            self.draw.rectangle([0, self.last_position, 3840, y_position], fill=color)
            self.last_position = y_position
    
    def run(self):
        self.createStripes()
        self.flag.save("flag.png")