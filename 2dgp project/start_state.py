import game_framework
import title_state
from pico2d import *
import game_world

name = "StartState"

Start_BG_image = None
Time_to_change_state = 4.0

def enter():
    global Start_BG_image
    Start_BG_image = StartBGIMG()
    game_world.add_object(Start_BG_image , 0)

    hide_cursor()
    Start_BG_image.BGM.play()


def exit():
    global Start_BG_image
    #Start_BG_image.BGM.stop()
    game_world.remove_object(Start_BG_image)

def update():
    global Time_to_change_state
    #일정 시간 경과 후 타이틀 화면으로 이동
    if (get_time()>Time_to_change_state):
        game_framework.change_state(title_state)


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

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





class StartBGIMG():
    image = None
    width = 800
    height = 600

    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\Start\\start.png')
        self.BGM = load_music('resources\\Sound\\SoundTrack\\Main Menu.mp3')
        self.BGM.set_volume(32)

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.clip_draw(0, 0, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)



