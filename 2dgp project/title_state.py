import game_framework
import difficulty_selection_state
import IMG_class
import cursor_class
import game_world
from pico2d import *

name = "TitleState"

# 이미지 파일
Title_BG_img = None
Title_start_text_img = None
Title_exit_text_img = None
# 이미지 객체
Title_start = None
Title_start_mouse_on = None
Title_exit = None
Title_exit_mouse_on = None


def enter():
    global Title_BG_img
    global Title_start_text_img, Title_exit_text_img
    global Title_start, Title_start_mouse_on
    global Title_exit, Title_exit_mouse_on
    global Title_BG_img
    global Title_start_text_img
    global Title_exit_text_img



    Title_BG_img = load_image('resources\\Title\\Background\\Title_BG.png')
    Title_start_text_img = load_image('resources\\Title\\Start\\start.png')
    Title_exit_text_img = load_image('resources\\Title\\Exit\\exit.png')


    # 초기 마우스 좌표
    cursor_class.mx = 800/2
    cursor_class.my = 600/2
    Title_start_text_img = None
    Title_exit_text_img = None

    # 객체 생성!
    Title_start = IMG_class.MenuStartIMG()
    Title_start_mouse_on =IMG_class.MenuStartMouseOnIMG()
    Title_exit = IMG_class.MenuExitIMG()
    Title_exit_mouse_on = IMG_class.MenuExitMouseOnIMG()

    cursor_class.cursor = cursor_class.Cursor(800 / 2, 600 / 2)

    game_world.add_object(Title_start,0)
    game_world.add_object(Title_start_mouse_on,0)
    game_world.add_object(Title_exit,0)
    game_world.add_object(Title_exit_mouse_on,0)
    game_world.add_object(Title_start,0)
    game_world.add_object(cursor_class.cursor,1)

def exit():
    game_world.clear()
    global Title_BG_img
    global Title_start_text_img
    global Title_exit_text_img
    del Title_BG_img
    del Title_start_text_img
    del Title_exit_text_img

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
            # 게임 시작
            if Title_start.mouse_on:

                game_framework.change_state(difficulty_selection_state)
            # 게임 종료
            elif Title_exit.mouse_on:
                game_framework.quit()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    global Title_start_text_img
    global Title_exit_text_img
    global Title_BG_img
    global Title_start_text_img
    global Title_exit_text_img

    clear_canvas()
    if   Title_BG_img!=None:
        Title_BG_img.draw(400, 300)

    for game_object in game_world.all_objects():
        game_object.draw()

    if Title_start_text_img != None:
        Title_start_text_img.draw(200, 480)
    if Title_exit_text_img != None:
        Title_exit_text_img.draw(550, 180)

    update_canvas()

def pause():
    pass


def resume():
    pass






