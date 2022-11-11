from pico2d import *
import game_framework
from background import Background
from miner import Miner
from gem import Gem

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            miner.handle_event(event)

background = None
miner = None
gem = None
running = True

def enter():
    global background, miner, gem
    background = Background()
    miner = Miner()
    gem = Gem()
    # running = True

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