from pico2d import *
import game_world

class Claw:
    image = None

    def __init__(self, x=800, y=300, v=1):
        if Claw.image == None:
            Claw.image = load_image('claw.png')
        self.x, self.y, self.v = x, y, v

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.v

        if self.y < 25 or self.y > 575:
            game_world.remove_object(self)