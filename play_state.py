from pico2d import *
import random
import game_framework

class Background:
    def __init__(self):
        self.image = load_image('Background1.png')

    def draw(self):
        self.image.draw(400, 300)

class Miner:
    def __init__(self):
        self.x, self.y = 400, 530
        self.frame = 0
        self.dir = 1
        self.image_right = load_image('miner_run_right.png')
        self.image_left = load_image('miner_run_left.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir = 1
                    self.x += 10
                elif event.key == SDLK_LEFT:
                    self.dir = -1
                    self.x -= 10

        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image_right.clip_draw(self.frame * 153, 0, 150, 170, self.x, self.y, 60, 60)
        else:
            self.image_left.clip_draw(self.frame * 154, 0, 150, 170, self.x, self.y, 60, 60)

class Gem:
    def __init__(self):
        self.gold_image = load_image('gold.png')
        self.goldcoordx, self.goldcoordy = random.randint(50, 500), random.randint(50, 480)

        self.big_gold_image = load_image('gold2.png')
        self.biggoldcoordx, self.biggoldcoordy = random.randint(50, 500), random.randint(150, 400)

        self.stone_image = load_image('stone1.png')
        self.stonecoordx, self.stonecoordy = random.randint(50, 500), random.randint(100, 480)

        self.big_stone_image = load_image('stone2.png')
        self.bigstonecoordx, self.bigstonecoordy = random.randint(50, 500), random.randint(150, 400)

        self.diamond_image = load_image('diamond.png')
        self.diamondcoordx, self.diamondcoordy = random.randint(50, 500), random.randint(100, 480)

        self.bomb_image = load_image('bomb.png')
        self.bombcoordx, self.bombcoordy = random.randint(50, 500), random.randint(70, 480)

    def draw(self):
        self.gold_image.draw(self.goldcoordx, self.goldcoordy)
        self.big_gold_image.draw(self.biggoldcoordx, self.biggoldcoordy)
        self.stone_image.draw(self.stonecoordx, self.stonecoordy)
        self.big_stone_image.draw(self.bigstonecoordx, self.bigstonecoordy)
        self.diamond_image.draw(self.diamondcoordx, self.diamondcoordy)
        self.bomb_image.draw(self.bombcoordx, self.bombcoordy)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

background = None
miner = None
gem = None
running = True

def enter():
    global background, miner, gem, running
    background = Background()
    miner = Miner()
    gem = Gem()
    running = True

def exit():
    global gem, background
    del gem
    del background

def update():
    miner.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    background.draw()
    miner.draw()
    gem.draw()

def pause():
    pass

def resume():
    pass