from pico2d import *
import game_world

RD, LD, RU, LU, DD, DU, UD, UU= range(8)
key_event_table = {
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYUP, SDLK_UP): UU,
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
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)
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
        self.x += (self.dir * 0.6)
        self.x = clamp(0+25, self.x, 1200-25)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.draw(self.x, self.y)
        elif self.dir == 1:
            self.image.draw(self.x, self.y)
        pass



class DOWN:
    @staticmethod
    def enter(self, event):
        if event == DD:
            self.ddir -= 1
        elif event == UD:
            self.ddir += 1
        elif event == DU:
            self.ddir += 1
        elif event == UU:
            self.ddir -= 1
        pass

    @staticmethod
    def exit(self, event):

        pass

    @staticmethod
    def do(self):
        self.y += (self.ddir * 1)
        self.y = clamp(0+25, self.y, 750-25)
        pass

    @staticmethod
    def draw(self):
        self.image.draw(self.x, self.y)
        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, DD: DOWN, DU: DOWN, UD: DOWN, UU: DOWN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, DU: RUN, UU: RUN, DD: RUN, UD: RUN},
    DOWN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, DU: IDLE, UU: IDLE, DD: IDLE, UD: IDLE}
}



class Claw:

    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def __init__(self):
        self.x, self.y = 600, 750
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.ddir = 0
        self.image = load_image('claw.png')
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

    def handle_collision(self, other, group):
        pass