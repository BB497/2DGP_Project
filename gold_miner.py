import pico2d
import game_framework
import play_state

pico2d.open_canvas(1200, 900)
game_framework.run(play_state)
pico2d.close_canvas()