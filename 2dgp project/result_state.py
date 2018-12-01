import game_world
from pico2d import *
import game_framework
import main_state
import IMG_class
import title_state

name = "ResultState"

Result_BG_IMG = None
Result_exit_text_img = None
Result_exit_img = None
Result_exit_mouse_on_img = None

def enter():
    global Result_BG_IMG
    global Result_exit_text_img,Result_exit_img,Result_exit_mouse_on_img

    Result_BG_IMG = ResultBGIMG()
    Result_exit_img = ResultExitIMG()
    Result_exit_mouse_on_img = ResultExitMouseOnIMG()
    Result_exit_text_img = ResultExitText()

    game_world.add_object(Result_BG_IMG, 0)
    game_world.add_object(Result_exit_img, 0)
    game_world.add_object(Result_exit_mouse_on_img, 0)
    game_world.add_object(Result_exit_text_img, 0)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def handle_events():
    global Result_exit_img

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
             if Result_exit_img.mouse_on is True:
                 game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
                # 마우스 좌표 업데이트
                game_world.update_mouse_point(event.x, event.y)

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

def pause(): pass


def resume(): pass




############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

class ResultBGIMG():
    image = None
    width = 800
    height = 600

    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\Title\\Background\\Title_BG.png')
            self.font =  load_font('font\\starcraft.TTF', 20)
            self.clear_stage = main_state.stage_level - 1

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.clip_draw(0, 0, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)


class  ResultExitIMG():
    image = None
    width = 184
    height = 128
    max_frame = 50
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = game_world.screen_x - 158
        self.y = 122

        self.frame = IMG_class.Frame(self.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if self.image == None:
            self.image = [load_image('resources\\Title\\Exit\\exit%d%d.png' % (i // 10, i % 10))  for i in range(0, self.max_frame)]

    def handle_events(self):
        pass

    def update(self):
        self.frame.update()
        if (self.x - self.width / 2 <= game_world.mx <= self.x + self.width / 2) and (
                self.y - self.height / 2 <= game_world.my <= self.y + self.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == True:
                self.mouse_on = False

    def draw(self):
            self.image[(int)(self.frame.current_frame)].draw(self.x, self.y)

class  ResultExitMouseOnIMG():
    image = None
    width = 184
    height = 128
    max_frame = 30
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = game_world.screen_x - 158
        self.y = 122

        self.frame = IMG_class.Frame(self.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if self.image == None:
            self.image = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, self.max_frame)]

    def handle_events(self):
        pass

    def update(self):
        self.frame.update()
        if (self.x - self.width / 2 <= game_world.mx <= self.x + self.width / 2) and (
                self.y - self.height / 2 <= game_world.my <= self.y + self.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
                self.frame.current_frame = 0
        else:
            if self.mouse_on == True:
                self.mouse_on = False

    def draw(self):
        if self.mouse_on == True:
            self.image[(int)(self.frame.current_frame)].draw(self.x, self.y)

class  ResultExitText():
    image = None
    width = 200
    height = 100

    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\Title\\Exit\\exit.png')

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.draw(game_world.screen_x - 200, 180)


############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################



