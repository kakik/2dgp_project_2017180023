import IMG_class
from pico2d import*
import game_framework
import difficulty_selection_state

class Observer():
    image = None
    width = 36
    height = 34
    max_frame = 27
    ACTION_PER_TIME = 0.5

    acceleration = 0.1
    max_velocity = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocity = 0.0
        self.frame = IMG_class.Frame(Observer.max_frame,1)
        self.frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.velocity_up_interval = 0
        self.velocity_down_interval = 0
        self.t = 0.0

        if Observer.image == None:
            Observer.image = [load_image('resources\\Observer\\%d%d.png' % (i // 10, i % 10)) for i in range(0, 15)]

    def get_events(self):
        pass

    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()

        if self.t >0:
            pass


    def draw(self):
        if 15 <= self.frame.current_frame:
            Observer.image[(int)(28- self.frame.current_frame)].composite_draw(3.141595653589793238,'v',self.x,self.y,self.width, self.height )
        else:
            Observer.image[(int)(self.frame.current_frame)].draw(self.x, self.y)



class Wraith():
    image = None
    width = 52
    height = 44
    max_frame = 31
    ACTION_PER_TIME = 0.5

    acceleration = 0.1
    max_velocity = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0.0
        self.frame = IMG_class.Frame(Wraith.max_frame, 1)
        self.frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.velocity_up_interval = 0
        self.velocity_down_interval = 0
        self.t = 0.0

        if Wraith.image == None:
            Wraith.image = [load_image('resources\\Wraith\\%d%d.png' % (i // 10, i % 10)) for i in range(0, 17)]

    def get_events(self):
        pass

    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()

        if self.t > 0:
            pass

    def draw(self):
        if 17 <= self.frame.current_frame:
            Wraith.image[(int)(32 - self.frame.current_frame)].composite_draw(3.141595653589793238, 'v', self.x,
                                                                                self.y, self.width, self.height)
        else:
            Wraith.image[(int)(self.frame.current_frame)].draw(self.x, self.y)




class Scourge():
    image = None
    width = 31
    height = 27
    max_frame = 16
    ACTION_PER_TIME = 0.5

    acceleration = 0.1
    max_velocity = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0.0
        self.frame = IMG_class.Frame(Scourge.max_frame, 1)
        self.frame.current_frame = 0
        self.IDLE_frame = IMG_class.Frame(4, 2)
        self.IDLE_frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.velocity_up_interval = 0
        self.velocity_down_interval = 0
        self.t = 0.0

        if Scourge.image == None:
            Scourge.image = load_image('resources\\Scourge\\Scourge.png' )

    def get_events(self):
        pass

    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()

        if self.t > 0:
            pass

        self.IDLE_frame.update()

    def draw(self):
        if 9 <= self.frame.current_frame:
            Scourge.image.clip_composite_draw((self.width+3)*(16-(int)(self.frame.current_frame))+2,369-((self.height+3)*(int)(self.IDLE_frame.current_frame+1)-1),self.width,self.height-2,3.141595653589793238, 'v', self.x,
                                                                                self.y, self.width, self.height)
        else:
            Scourge.image.clip_draw((self.width+3)*(int)(self.frame.current_frame)+2,369-((self.height+3)*(int)(self.IDLE_frame.current_frame+1)-1), self.width, self.height-2,self.x,
                                                                                self.y)



