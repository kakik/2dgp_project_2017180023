import game_framework
import title_state
from pico2d import *
import game_world

name = "StartState"
image = None



def enter():
    global image
    image = load_image('resources\\Start\\start.png')
    hide_cursor()


def exit():
    global image
    del (image)


def update():

    if (get_time()>3.0):
        game_framework.change_state(title_state)


def draw():
    global image
    clear_canvas()
    image.clip_draw(0,0,game_world.screen_x, game_world.screen_y, game_world.screen_x/2, game_world.screen_y/2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def pause(): pass


def resume(): pass






