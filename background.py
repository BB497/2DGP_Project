from pico2d import *

class Background:
    def __init__(self):
        self.Bg_image = load_image('Background1.png')
        self.Ground_image = load_image('ground.png')
    def draw(self):
        self.Bg_image.draw(600, 450, 1200, 900)
        for i in range(25):
            self.Ground_image.draw(i*50, 750, 50, 50)

        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return 0, 725, 1200-1, 780