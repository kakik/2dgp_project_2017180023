import game_framework
import difficulty_selection_state
import IMG_class
import cursor_class
import game_world
from pico2d import *

name = "TitleState"

# 이미지 객체
Title_BG_img = None
Title_exit_text_img = None
Title_exit = None
Title_exit_mouse_on = None


def enter():
    global Title_BG_img
    global  Title_exit_text_img
    global Title_start, Title_start_mouse_on
    global Title_exit, Title_exit_mouse_on

    # 초기 마우스 좌표
    game_world.mx = game_world.screen_x / 2
    game_world.my = game_world.screen_y / 2

    # 객체 생성!
    Title_BG_img = MenuBGIMG()
    Title_start = MenuStartIMG()
    Title_start_mouse_on =MenuStartMouseOnIMG()
    Title_exit = MenuExitIMG()
    Title_exit_mouse_on = MenuExitMouseOnIMG()
    Title_start_text_img = MenuStartText()
    Title_exit_text_img = MenuExitText()

    #월드에 객체 추가!
    game_world.add_object(Title_BG_img, 0)
    game_world.add_object(Title_start,0)
    game_world.add_object(Title_start_mouse_on,0)
    game_world.add_object(Title_exit,0)
    game_world.add_object(Title_exit_mouse_on,0)
    game_world.add_object(Title_start_text_img, 0)
    game_world.add_object(Title_exit_text_img, 0)

    #커서 추가
    game_world.cursor = cursor_class.Cursor(game_world.screen_x / 2, game_world.screen_y / 2)
    game_world.add_object(game_world.cursor, 1)


def exit():
    game_world.clear_except_cursor()



def handle_events():
    global Title_BG_img

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
            # 게임 시작
            if Title_start.mouse_on:
                Title_BG_img.Mouse_down_wav.play()
                game_framework.change_state(difficulty_selection_state)
            # 게임 종료
            elif Title_exit.mouse_on:
                #Title_BG_img.Mouse_down_wav.play()
                game_framework.quit()




def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


def pause():
    pass


def resume():
    pass


############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################


class MenuBGIMG():
    image = None
    width = 800
    height = 600

    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\Title\\Background\\Title_BG.png')
            self.BGM = load_music('resources\\Sound\\SoundTrack\\Terran - 1.mp3')
            self.BGM.set_volume(32)
            self.Mouse_down_wav = load_wav('resources\\Sound\\Glue\\mousedown2.wav')
            self.Mouse_down_wav.set_volume(32)
            #self.BGM.play()

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.clip_draw(0, 0, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)

class MenuStartIMG():
    image = None
    width = 320
    height = 116
    max_frame = 35
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = 240
        self.y = game_world.screen_y - 162

        self.frame = IMG_class.Frame(self.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if self.image == None:
            self.image = [load_image('resources\\Title\\Start\\single%d%d.png'%(i//10, i%10)) for i in range(0, self.max_frame)]


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



class MenuExitIMG():
    image = None
    width = 184
    height = 128
    max_frame = 50
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = game_world.screen_x - 208
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


class MenuStartMouseOnIMG():
    image = None
    width = 320
    height = 116
    max_frame = 60
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = 240
        self.y = game_world.screen_y - 162

        self.frame = IMG_class.Frame(self.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if self.image == None:
            self.image =[load_image('resources\\Title\\Start\\English\\singleon%d%d.png' % (i // 10, i % 10)) for i in range(0, self.max_frame)]

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

class MenuExitMouseOnIMG():
    image = None
    width = 184
    height = 128
    max_frame = 30
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = game_world.screen_x - 208
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

class MenuStartText():
    image = None
    width = 200
    height = 100

    def __init__(self):
        if self.image == None:
            self.image =load_image('resources\\Title\\Start\\start.png')

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.draw(200, game_world.screen_y - 100)

class MenuExitText():
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
            self.image.draw(game_world.screen_x - 250, 180)




############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################



