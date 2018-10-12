import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('resources\\Start\\start.png')
    hide_cursor()


def exit():
    global image
    del (image)


def update():
    global logo_time

    if (logo_time > 1.5):
        logo_time = 0
        game_framework.change_state(title_state)

    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
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






