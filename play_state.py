from pico2d import *
import game_framework
import game_world

from background import Background
from miner import Miner
from claw import Claw
from gem import Gold, BigGold, Stone, BigStone, Diamond

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            claw.handle_event(event)
            miner.handle_event(event)

background = None
miner = None
claw = None
gems = []
running = True

def enter():
    global background, miner, claw
    background = Background()
    miner = Miner()
    claw = Claw()
    game_world.add_object(miner, 1)
    game_world.add_object(background, 0)
    game_world.add_object(claw, 1)

    global gems
    gems = [Gold() for i in range(6)] + [BigGold() for i in range(5)] +\
           [Diamond() for i in range(2)] + [Stone() for i in range(7)] + [BigStone() for i in range(5)]
    game_world.add_objects(gems, 0)

    game_world.add_collision_pairs(claw, gems, 'claw:gem')


def exit():
    # global gem, background
    # del gem
    # del background
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('Collision', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
    # background.draw()
    # miner.draw()
    # gem.draw()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def pause():
    pass

def resume():
    pass

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
