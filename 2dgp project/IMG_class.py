import cursor_class
from pico2d import *
import game_framework

class MenuStartIMG():
    image = None
    width = 320
    height = 116
    max_frame = 35
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = 240
        self.y = 438

        self.frame = Frame(MenuStartIMG.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if MenuStartIMG.image == None:
            MenuStartIMG.image = [load_image('resources\\Title\\Start\\single%d%d.png'%(i//10, i%10)) for i in range(0, MenuStartIMG.max_frame)]


    def handle_events(self):
        pass

    def update(self):
        self.frame.update()
        if (self.x - MenuStartMouseOnIMG.width / 2 <= cursor_class.mx <= self.x + MenuStartMouseOnIMG.width / 2) and (
                self.y - MenuStartMouseOnIMG.height / 2 <= cursor_class.my <= self.y + MenuStartMouseOnIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == True:
                self.mouse_on = False

    def draw(self):
        MenuStartIMG.image[(int)(self.frame.current_frame)].draw(self.x, self.y)



class MenuExitIMG():
    image = None
    width = 184
    height = 128
    max_frame = 50
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = 592
        self.y = 122

        self.frame = Frame(MenuExitIMG.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if MenuExitIMG.image == None:
            MenuExitIMG.image = [load_image('resources\\Title\\Exit\\exit%d%d.png' % (i // 10, i % 10))  for i in range(0, MenuExitIMG.max_frame)]

    def handle_events(self):
        pass

    def update(self):
        self.frame.update()
        if (self.x - MenuStartMouseOnIMG.width / 2 <= cursor_class.mx <= self.x + MenuStartMouseOnIMG.width / 2) and (
                self.y - MenuStartMouseOnIMG.height / 2 <= cursor_class.my <= self.y + MenuStartMouseOnIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == True:
                self.mouse_on = False

    def draw(self):
        MenuExitIMG.image[(int)(self.frame.current_frame)].draw(self.x, self.y)


class MenuStartMouseOnIMG():
    image = None
    width = 320
    height = 116
    max_frame = 60
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = 240
        self.y = 438

        self.frame = Frame(MenuStartMouseOnIMG.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if MenuStartMouseOnIMG.image == None:
            MenuStartMouseOnIMG.image =[load_image('resources\\Title\\Start\\English\\singleon%d%d.png' % (i // 10, i % 10)) for i in range(0, MenuStartMouseOnIMG.max_frame)]

    def handle_events(self):
        pass

    def update(self):
        self.frame.update()
        if (self.x - MenuStartMouseOnIMG.width / 2 <= cursor_class.mx <= self.x + MenuStartMouseOnIMG.width / 2) and (
                self.y - MenuStartMouseOnIMG.height / 2 <= cursor_class.my <= self.y + MenuStartMouseOnIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
                self.frame.current_frame = 0
        else:
            if self.mouse_on == True:
                self.mouse_on = False

    def draw(self):
        if self.mouse_on == True:
            MenuStartMouseOnIMG.image[(int)(self.frame.current_frame)].draw(self.x, self.y)


class MenuExitMouseOnIMG():
    image = None
    width = 184
    height = 128
    max_frame = 30
    ACTION_PER_TIME = 0.5

    def __init__(self):
        self.x = 592
        self.y = 122

        self.frame = Frame(MenuExitMouseOnIMG.max_frame,self.ACTION_PER_TIME)
        self.mouse_on = False

        if MenuExitMouseOnIMG.image == None:
            MenuExitMouseOnIMG.image = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, MenuExitMouseOnIMG.max_frame)]

    def handle_events(self):
        pass

    def update(self):
        self.frame.update()
        if (self.x - MenuStartMouseOnIMG.width / 2 <= cursor_class.mx <= self.x + MenuStartMouseOnIMG.width / 2) and (
                self.y - MenuStartMouseOnIMG.height / 2 <= cursor_class.my <= self.y + MenuStartMouseOnIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
                self.frame.current_frame = 0
        else:
            if self.mouse_on == True:
                self.mouse_on = False

    def draw(self):
        if self.mouse_on == True:
            MenuExitMouseOnIMG.image[(int)(self.frame.current_frame)].draw(self.x, self.y)


class Frame:
    def __init__(self, max_frame, ACTION_PER_TIME):
        self.current_frame = 0
        self.max_frame = max_frame
        self.ACTION_PER_TIME = ACTION_PER_TIME

    def update(self):
        self.current_frame = (self.current_frame + (self.ACTION_PER_TIME*self.max_frame*game_framework.frame_time)) % self.max_frame
