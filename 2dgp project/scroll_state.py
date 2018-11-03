import random
import game_world
import Unit_class
import game_framework
from pico2d import *
import cursor_class
import game_framework
import title_state
from background import FixedBackground as Background

name = "scroll_state"

background = None

def create_world():
    global  background
    background = Background()

    # fill here



def destroy_world():
    global boy, background
    del(boy)
    del(background)

def enter():
    pass

def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            # 마우스 좌표 업데이트
            cursor_class.update_mouse_point(event.x, event.y)

        elif event.type == SDL_MOUSEBUTTONDOWN:
           pass



def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






