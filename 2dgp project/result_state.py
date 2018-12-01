import game_world
from pico2d import *
import game_framework
import main_state
import IMG_class
import title_state

name = "ResultState"

Result_BG_IMG = None
Result_score_popup = None

def enter():
    global Result_BG_IMG
    global Result_score_popup

    Result_BG_IMG = ResultBGIMG()

    Result_score_popup= ResultScorePopup()
    game_world.add_object(Result_BG_IMG, 0)

    game_world.add_object(Result_score_popup, 1)

def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def handle_events():
    global Result_score_popup

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if Result_score_popup.is_mouse_on is True:
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

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.clip_draw(0, 0, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)



class ResultScorePopup():
    image = None
    width = 360
    height = 200
    draw_width = None
    draw_height = None
    move_down_speed_per_sec = None

    def __init__(self):
        if self.draw_width is None:
            self.draw_width = self.width / game_world.screen_x * 800
        if self.draw_height is None:
            self.draw_height = self.height / game_world.screen_y * 600
        if self.move_down_speed_per_sec is None:
            self.move_down_speed_per_sec = game_world.screen_y*1.5
        if self.image == None:
            self.image = load_image('resources\\UI\\popopup.png')

        self.x = game_world.screen_x/2
        self.y = game_world.screen_y + self.draw_height/2
        self.font = load_font('font\\starcraft.TTF', 20)
        self.clear_stage = main_state.stage_level - 1
        self.is_mouse_on = False



    def handle_events(self):
        pass

    def update(self):
        if self.y > game_world.screen_y /2:
            self.y -=  self.move_down_speed_per_sec*game_framework.frame_time
            if self.y < game_world.screen_y /2:
                self.y = game_world.screen_y / 2

        if (self.x - self.width / 2 <= game_world.mx <= self.x + self.width / 2) and (
                self.y - self.height / 2 <= game_world.my <= self.y + self.height / 2):
            if self.is_mouse_on is False:
                self.is_mouse_on = True
        else:
            if self.is_mouse_on is True:
                self.is_mouse_on = False

    def draw(self):
        if self.image != None:
            self.image.clip_draw(0, 0, self.width, self.height, self.x,
                                 int(self.y),self.draw_width, self.draw_height)

        self.font.draw( self.x-100, self.y, 'Clear Stage: %d' % (self.clear_stage), (0, 255, 0))



############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################



