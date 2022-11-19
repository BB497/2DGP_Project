from pico2d import *
import random

import game_world


class Gold:
    image = None

    def __init__(self):
        if Gold.image == None:
            Gold.image = load_image('gold.png')
        self.x, self.y = random.randint(50, 1200-50), random.randint(50, 725-50)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10

    def handle_collision(self, other, group):
        if group == 'claw:gem':
            game_world.remove_object(self)

class BigGold:
    image = None

    def __init__(self):
        if BigGold.image == None:
            BigGold.image = load_image('gold2.png')
        self.x, self.y = random.randint(50, 1200-50), random.randint(50, 725-200)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-25, self.y-25, self.x+25, self.y+25

    def handle_collision(self, other, group):
        if group == 'claw:gem':
            game_world.remove_object(self)

class Stone:
    image = None

    def __init__(self):
        if Stone.image == None:
            Stone.image = load_image('stone1.png')
        self.x, self.y = random.randint(50, 1200-50), random.randint(50, 725-150)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10

    def handle_collision(self, other, group):
        if group == 'claw:gem':
            game_world.remove_object(self)


class BigStone:
    image = None

    def __init__(self):
        if BigStone.image == None:
            BigStone.image = load_image('stone2.png')
        self.x, self.y = random.randint(50, 1200-50), random.randint(50, 725-200)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-25, self.y-25, self.x+25, self.y+25

    def handle_collision(self, other, group):
        if group == 'claw:gem':
            game_world.remove_object(self)



class Diamond:
    image = None

    def __init__(self):
        if Diamond.image == None:
            Diamond.image = load_image('diamond.png')
        self.x, self.y = random.randint(50, 1200-50), random.randint(50, 725-150)

    def draw(self):
        self.image.draw(self.x, self.y, 15, 20)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5

    def handle_collision(self, other, group):
        if group == 'claw:gem':
            game_world.remove_object(self)