from pico2d import *
import cursor_class
import game_framework
import game_world
import Unit_class
import main_state

name = "DifficultySelectionState"

Difficulty_BG_img = None
mx, my = 0, 0

observer = None
wraith = None
scourge = None
def enter():
    global Difficulty_BG_img
    global observer,wraith, scourge

    Difficulty_BG_img = load_image('resources\\Title\\Background\\Title_BG.png')

    scourge = Unit_class.Scourge(game_world.screen_x/3*0.5, game_world.screen_y/3*1.5)
    observer = Unit_class.Observer(game_world.screen_x/3*1.5, game_world.screen_y/3*1.5)
    wraith = Unit_class.Wraith(game_world.screen_x/3*2.5, game_world.screen_y/3*1.5)

    game_world.add_object(scourge, 1)
    game_world.add_object(observer, 1)
    game_world.add_object(wraith, 1)


def exit():
    global Difficulty_BG_img
    del Difficulty_BG_img
    # game_world.clear()
    game_world.remove_object(scourge)
    game_world.remove_object(observer)
    game_world.remove_object(wraith)

def pause():
    pass


def resume():
    pass


def handle_events():
    global observer, wraith, scourge
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            # 마우스 좌표 업데이트
            game_world.update_mouse_point(event.x, event.y)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if scourge.x-scourge.width/2 < game_world.mx <scourge.x+scourge.width/2 and scourge.y-scourge.height/2 < game_world.my <scourge.y+scourge.height/2:
                main_state.player = Unit_class.Player()
                Unit_class.set_player_unit( main_state.player, 1)
                game_world.add_object( main_state.player, 1)
                game_framework.change_state(main_state)

            elif observer.x - observer.width / 2 < game_world.mx < observer.x + observer.width / 2 and observer.y - observer.height / 2 < game_world.my < observer.y + observer.height / 2:
                main_state.player = Unit_class.Player()
                Unit_class.set_player_unit( main_state.player, 2)
                game_world.add_object( main_state.player, 1)
                game_framework.change_state(main_state)

            elif wraith.x - wraith.width / 2 < game_world.mx < wraith.x + wraith.width / 2 and wraith.y - wraith.height / 2 < game_world.my < wraith.y + wraith.height / 2:
                main_state.player = Unit_class.Player()
                Unit_class.set_player_unit( main_state.player,3)
                game_world.add_object( main_state.player, 1)
                game_framework.change_state(main_state)


def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()

    if Difficulty_BG_img != None:
        Difficulty_BG_img.clip_draw(0,0,game_world.screen_x,game_world.screen_y,game_world.screen_x/2, game_world.screen_y/2)

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()







