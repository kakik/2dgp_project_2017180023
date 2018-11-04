import game_world
import Unit_class
import game_framework
from pico2d import *
import Unit_class
import game_framework
import title_state

player = None
background_image = None
def enter():
    global background_image
    background_image = load_image('resources\\TileMap\\Map.png')
    for i in range(0,9):
        for j in range(0,9):
            for k in range (0,4):
                game_world.add_object(Unit_class.Observer(game_world.map_x/9*(j+0.5),game_world.map_y/9*(i+0.5)),1)


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global player
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_w:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = 1
                elif game_world.screen_scroll_y == -1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_a:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = -1
                elif game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = 1
            elif event.key == SDLK_s:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = -1
                elif game_world.screen_scroll_y == 1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_d:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = 1
                elif game_world.screen_scroll_x == -1:
                    game_world.screen_scroll_x = 0

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = -1
                elif game_world.screen_scroll_y == 1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_a:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = 1
                elif game_world.screen_scroll_x == -1:
                    game_world.screen_scroll_x = 0
            elif event.key == SDLK_s:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = 1
                elif game_world.screen_scroll_y == -1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_d:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = -1
                elif game_world.screen_scroll_x == 1:
                    game_world.screen_scroll_x = 0


        if event.type == SDL_MOUSEMOTION:
            # 마우스 좌표 업데이트
            game_world.update_mouse_point(event.x, event.y)

        if event.type == SDL_MOUSEBUTTONDOWN:
            player.get_events()





def update():
    game_world.update_screen_xy()
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    global background_image
    clear_canvas()
    background_image.clip_draw(game_world.screen_coord_x, game_world.screen_coord_y, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






