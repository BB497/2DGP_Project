from pico2d import *
import game_world
from claw import Claw

RD, LD, RU, LU, DOWN = range(5)
key_event_table = {
    (SDL_KEYDOWN, SDLK_DOWN): DOWN,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}

class IDLE:
    @staticmethod
    def enter(self, event):
        # print('ENTER IDLE')
        self.dir = 0
        pass

    @staticmethod
    def exit(self, event):
        # print('exit idle')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 9
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_idler.clip_draw(self.frame*130, 0, 131, 177,
                                       self.x, self.y, 65, 65)
        else:
            self.image_idlel.clip_draw(self.frame*130, 0, 131, 177,
                                       self.x, self.y, 65, 65)
        pass

class RUN:
    @staticmethod
    def enter(self, event):
        # print('enter run')

        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    @staticmethod
    def exit(self, event):
        # print('exit run')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += (self.dir * 0.6)
        self.x = clamp(0+25, self.x, 1200-25)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image_left.clip_draw(self.frame*153, 0, 150, 170,
                                       self.x, self.y, 65, 65)
        elif self.dir == 1:
            self.image_right.clip_draw(self.frame*154, 0, 150, 170,
                                      self.x, self.y, 65, 65)
        pass

next_state = {
    IDLE: {RU: RUN, LU:RUN, RD: RUN, LD: RUN, DOWN: IDLE},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, DOWN: RUN}
}



class Miner:

    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def __init__(self):
        self.x, self.y = 600, 800
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image_right = load_image('miner_run_right.png')
        self.image_left = load_image('miner_run_left.png')
        self.image_idler = load_image('miner_idle_right.png')
        self.image_idlel = load_image('miner_idle_left.png')
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        # self.font.draw(self.x-60, self.y+50,
        #                '(Time: %3.2f)' % get_time(), (255,255,0))
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x-30, self.y-30, self.x+30, self.y+30