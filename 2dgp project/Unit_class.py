import IMG_class
from pico2d import*
import game_framework
import difficulty_selection_state
import main_state
import game_world
import random
import math

def set_player_unit(player, key):
    if key == 1:
        player.unit = Scourge(100 ,100)
    elif key == 2:
        player.unit = Observer(100 ,100)
    elif key == 3:
        player.unit = Wraith(100 ,100)


class Player():

    def __init__(self):
        self.unit = None

    def get_events(self):
        self.unit.get_events()

    def update(self):
        self.unit.update()


    def draw(self):
        self.unit.draw()


class Observer():
    image = None
    width = 36
    height = 34
    max_frame = 28
    ACTION_PER_TIME = 0.5
    velocity = 100.0

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame = IMG_class.Frame(Observer.max_frame,1)
        self.frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.curr_t = 0.0
        self.to_t = 0.0

        if Observer.image == None:
            Observer.image = [load_image('resources\\Observer\\%d%d.png' % (i // 10, i % 10)) for i in range(0, 15)]

    def get_events(self):
        pass

    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()
        else:
            if self.curr_t < 0.0000001:
                self.set_random_move_point()
            else:
                self.move()




    def draw(self):
        if 15 <= self.frame.current_frame:
            Observer.image[(int)(28- self.frame.current_frame)].composite_draw(3.141595653589793238,'v',self.x-game_world.screen_x,self.y-game_world.screen_y ,self.width, self.height )
        else:
            Observer.image[(int)(self.frame.current_frame)].draw(self.x-game_world.screen_x, self.y-game_world.screen_y )

    def set_random_move_point(self):
        x_distance = random.randint(0, 1000) - 500
        y_distance = random.randint(0, 1000) - 500

        if self.x + x_distance < 0 + self.width / 2:
            print('a')
            x_distance = 0 - self.x + self.width
        elif game_world.map_x - self.width / 2 < self.x + x_distance:
            print('b')
            x_distance = game_world.map_x - self.x - self.width

        if self.y + y_distance < 0 + self.height / 2:
            y_distance = 0 - self.y + self.height
        elif game_world.map_y - self.height / 2 < self.y + y_distance:
            y_distance = game_world.map_y - self.y - self.height

        self.to_t = math.sqrt(x_distance ** 2 + y_distance ** 2) / self.velocity + get_time()
        self.x_velocity = x_distance / (self.to_t - get_time())
        self.y_velocity = y_distance / (self.to_t - get_time())
        self.curr_t = get_time()
        self.frame.direction_update(self.x_velocity, self.y_velocity)
        self.to_x = self.x + self.x_velocity
        self.to_y = self.y + self.y_velocity

    def move(self):
        # 이동 종료
        if (self.curr_t) > self.to_t:
            self.to_x = self.x
            self.to_y = self.y
            self.x_velocity = 0
            self.y_velocity = 0
            self.curr_t = 0.0
            self.to_t = 0.0
            self.set_random_move_point()
        else:
            self.x += self.x_velocity * (get_time() - self.curr_t)
            self.y += self.y_velocity * (get_time() - self.curr_t)
            self.curr_t = get_time()




class Wraith():
    image = None
    width = 52
    height = 44
    max_frame = 32
    ACTION_PER_TIME = 0.5
    velocity = 200.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = IMG_class.Frame(Wraith.max_frame, 1)
        self.frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.curr_t = 0.0
        self.to_t = 0.0

        if Wraith.image == None:
            Wraith.image = [load_image('resources\\Wraith\\%d%d.png' % (i // 10, i % 10)) for i in range(0, 17)]

    def get_events(self):
        pass

    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()
        else:
            if self.curr_t < 0.0000001:
                self.set_random_move_point()
            else:
                self.move()



    def draw(self):
        if 17 <= self.frame.current_frame:
            Wraith.image[(int)(32 - self.frame.current_frame)].composite_draw(3.141595653589793238, 'v', self.x-game_world.screen_x,
                                                                                self.y-game_world.screen_y , self.width, self.height)
        else:
            Wraith.image[(int)(self.frame.current_frame)].draw(self.x-game_world.screen_x, self.y-game_world.screen_y )



    def set_random_move_point(self):
        x_distance = random.randint(0, 1000) - 500
        y_distance = random.randint(0, 1000) - 500

        if self.x + x_distance < 0 + self.width / 2:
            print('a')
            x_distance = 0 - self.x + self.width
        elif game_world.map_x - self.width / 2 < self.x + x_distance:
            print('b')
            x_distance = game_world.map_x - self.x - self.width

        if self.y + y_distance < 0 + self.height / 2:
            y_distance = 0 - self.y + self.height
        elif game_world.map_y - self.height / 2 < self.y + y_distance:
            y_distance = game_world.map_y - self.y - self.height

        self.to_t = math.sqrt(x_distance ** 2 + y_distance ** 2) / self.velocity + get_time()
        self.x_velocity = x_distance / (self.to_t-get_time())
        self.y_velocity = y_distance / ( self.to_t-get_time())
        self.curr_t = get_time()
        self.frame.direction_update(self.x_velocity, self.y_velocity)
        self.to_x = self.x+self.x_velocity
        self.to_y = self.y + self.y_velocity


    def move(self):
        # 이동 종료
        if (self.curr_t) > self.to_t:
            self.to_x = self.x
            self.to_y = self.y
            self.x_velocity = 0
            self.y_velocity = 0
            self.curr_t = 0.0
            self.to_t = 0.0
            self.set_random_move_point()
        else:
            self.x += self.x_velocity * (get_time() - self.curr_t)
            self.y += self.y_velocity * (get_time() - self.curr_t)
            self.curr_t = get_time()





class Scourge():
    image = None
    width = 31
    height = 27
    max_frame = 16
    ACTION_PER_TIME = 0.5
    velocity = 200.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = IMG_class.Frame(Scourge.max_frame, 1)
        self.frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.curr_t = 0.0
        self.to_t = 0.0

        self.IDLE_frame = IMG_class.Frame(4, 2)
        self.IDLE_frame.current_frame = 0

        if Scourge.image == None:
            Scourge.image = load_image('resources\\Scourge\\Scourge.png' )

    def get_events(self):
        pass


    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()
        else:
            if self.curr_t < 0.0000001:
                self.set_random_move_point()
            else:
                self.move()

        self.IDLE_frame.update()


    def draw(self):
        if 9 <= self.frame.current_frame:
            Scourge.image.clip_composite_draw((self.width+3)*(16-(int)(self.frame.current_frame))+2,369-((self.height+3)*(int)(self.IDLE_frame.current_frame+1)-1),
                                              self.width,self.height-2,3.141595653589793238, 'v', self.x-game_world.screen_x, self.y-game_world.screen_y , self.width, self.height)
        else:
            Scourge.image.clip_draw((self.width+3)*(int)(self.frame.current_frame)+2,369-((self.height+3)*(int)(self.IDLE_frame.current_frame+1)-1), self.width, self.height-2,self.x-game_world.screen_x,
                                                                                self.y-game_world.screen_y )

    def set_random_move_point(self):
        x_distance = random.randint(0, 1000) - 500
        y_distance = random.randint(0, 1000) - 500

        if self.x + x_distance < 0 + self.width / 2:
            print('a')
            x_distance = 0 - self.x + self.width
        elif game_world.map_x - self.width / 2 < self.x + x_distance:
            print('b')
            x_distance = game_world.map_x - self.x - self.width

        if self.y + y_distance < 0 + self.height / 2:
            y_distance = 0 - self.y + self.height
        elif game_world.map_y - self.height / 2 < self.y + y_distance:
            y_distance = game_world.map_y - self.y - self.height

        self.to_t = math.sqrt(x_distance ** 2 + y_distance ** 2) / self.velocity + get_time()
        self.x_velocity = x_distance / (self.to_t - get_time())
        self.y_velocity = y_distance / (self.to_t - get_time())
        self.curr_t = get_time()
        self.frame.direction_update(self.x_velocity, self.y_velocity)
        self.to_x = self.x + self.x_velocity
        self.to_y = self.y + self.y_velocity

    def move(self):
        # 이동 종료
        if (self.curr_t) > self.to_t:
            self.to_x = self.x
            self.to_y = self.y
            self.x_velocity = 0
            self.y_velocity = 0
            self.curr_t = 0.0
            self.to_t = 0.0
            self.set_random_move_point()
        else:
            self.x += self.x_velocity * (get_time() - self.curr_t)
            self.y += self.y_velocity * (get_time() - self.curr_t)
            self.curr_t = get_time()







