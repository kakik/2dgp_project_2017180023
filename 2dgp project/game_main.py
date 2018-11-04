import game_framework
import pico2d
import start_state
import game_world

pico2d.open_canvas(game_world.screen_x, game_world.screen_y)
game_framework.run(start_state)
pico2d.close_canvas()
