from pico2d import *
import random

class Gem:
    def __init__(self):
        self.gold_image = load_image('gold.png')
        self.goldcoordx, self.goldcoordy = \
            random.randint(50, 750), random.randint(50, 480)

        self.big_gold_image = load_image('gold2.png')
        self.biggoldcoordx, self.biggoldcoordy = \
            random.randint(50, 750), random.randint(150, 400)

        self.stone_image = load_image('stone1.png')
        self.stonecoordx, self.stonecoordy = \
            random.randint(50, 750), random.randint(100, 480)

        self.big_stone_image = load_image('stone2.png')
        self.bigstonecoordx, self.bigstonecoordy = \
            random.randint(50, 750), random.randint(150, 400)

        self.diamond_image = load_image('diamond.png')
        self.diamondcoordx, self.diamondcoordy = \
            random.randint(50, 750), random.randint(100, 480)

        self.bomb_image = load_image('bomb.png')
        self.bombcoordx, self.bombcoordy = \
            random.randint(50, 750), random.randint(70, 480)

    def draw(self):
        self.gold_image.draw(self.goldcoordx, self.goldcoordy)
        self.big_gold_image.draw(self.biggoldcoordx, self.biggoldcoordy)
        self.stone_image.draw(self.stonecoordx, self.stonecoordy)
        self.big_stone_image.draw(self.bigstonecoordx, self.bigstonecoordy)
        self.diamond_image.draw(self.diamondcoordx, self.diamondcoordy)
        self.bomb_image.draw(self.bombcoordx, self.bombcoordy)

    def update(self):
        pass