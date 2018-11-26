import IMG_class
from pico2d import*
import game_framework
import difficulty_selection_state
import main_state
import game_world
import random
import math

tile_size = 31

def set_player_unit(player, key):
    if key == 1:
        player.unit = Scourge(200 ,250)
    elif key == 2:
        player.unit = Observer(200 ,250)
    elif key == 3:
        player.unit = Wraith(200,250)


class Player():

    def __init__(self):
        self.unit = None
        self.under_unit_cursor_img =  load_image('resources\\Cursor\\cursor.png')

    def get_events(self):
        self.unit.set_move_point(game_world.mx,game_world.my)
        self.unit.get_events()

    def update(self):
        self.unit.move()
        self.unit.collision_check()
        # 이동 종료
        if (self.unit.curr_t) > self.unit.to_t:
            self.unit.to_x = self.unit.x
            self.unit.to_y = self.unit.y
            self.unit.x_velocity = 0
            self.unit.y_velocity = 0
            self.unit.curr_t = 0.0
            self.unit.to_t = 0.0

        if self.unit.__class__.__name__== 'Scourge':
            self.unit.IDLE_frame.update()




    def draw(self):
        self.under_unit_cursor_img.clip_draw(46, 232, 41, 41, self.unit.x - game_world.screen_coord_x, self.unit.y - game_world.screen_coord_y - self.unit.height / 5 - 10, self.unit.width, self.unit.height)
        self.unit.draw()

    def return_to_start_point(self):
        self.unit.x = 200
        self.unit.y = 250
        self.unit.to_x = 200
        self.unit.to_y = 250
        self.unit.x_velocity = 0
        self.unit.y_velocity = 0
        self.unit.curr_t = 0.0
        self.unit.to_t = 0.0

class Unit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = IMG_class.Frame(Observer.max_frame, 1)
        self.frame.current_frame = 0

        self.to_x = x
        self.to_y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.curr_t = 0.0
        self.to_t = 0.0

    def get_events(self):
        pass

    def update(self):
        if game_framework.stack[-1] == difficulty_selection_state:
            self.frame.update()
        else:

            self.move()
            # 이동 종료
            if (self.curr_t) > self.to_t:
                self.to_x = self.x
                self.to_y = self.y
                self.x_velocity = 0
                self.y_velocity = 0
                self.curr_t = 0.0
                self.to_t = 0.0
                self.set_random_move_point()

    def draw(self):
        pass

    def set_random_move_point(self):
        x_move_distance = random.randint(0, 1000) - 500
        y_move_distance = random.randint(0, 1000) - 500

        if self.x + x_move_distance < 0 + self.width / 2:
            x_move_distance = 0 - self.x + self.width
        elif game_world.map_x - self.width / 2 < self.x + x_move_distance:
            x_move_distance = game_world.map_x - self.x - self.width

        if self.y + y_move_distance < 0 + self.height / 2:
            y_move_distance = 0 - self.y + self.height
        elif game_world.map_y - self.height / 2 < self.y + y_move_distance:
            y_move_distance = game_world.map_y - self.y - self.height

        self.set_velocity(x_move_distance, y_move_distance)


    def set_move_point(self, to_x, to_y):
        self.set_velocity(to_x - self.x, to_y - self.y)


    def move(self):
        self.x += self.x_velocity * (get_time() - self.curr_t)
        self.y += self.y_velocity * (get_time() - self.curr_t)
        self.curr_t = get_time()

    def set_velocity(self, x_move_distance, y_move_distance):
        self.to_t = math.sqrt(x_move_distance ** 2 + y_move_distance ** 2) / self.velocity + get_time()
        self.x_velocity = x_move_distance / (self.to_t - get_time())
        self.y_velocity = y_move_distance / (self.to_t - get_time())
        self.curr_t = get_time()
        self.frame.direction_update(self.x_velocity, self.y_velocity)
        self.to_x = self.x + self.x_velocity
        self.to_y = self.y + self.y_velocity

    def collision_check(self):
        # 안전지역 체크
        if (tile_size * 4 <= self.x <= tile_size * 12) and (tile_size * 4 <= self.y <= tile_size * 12):
            #print("start_zone")
        # 안전지역 체크
            pass
        elif (tile_size * 4 <= self.x <= tile_size * 12) and (tile_size * 17 <= self.y <= tile_size * 25):
            #print("safe_zone")
        # 종료지역 체크
            pass
        elif (tile_size * 48 <= self.x <= tile_size * 56) and (tile_size * 48 <= self.y <= tile_size * 56):
            #print("clear")
            main_state.proceed_next_stage()
            game_world.reset_screen_xy()
        elif ((tile_size * 4 <= self.x <= tile_size * 56) and (tile_size * 4 <= self.y <= tile_size * 12)) or \
                ((tile_size * 48 <= self.x <= tile_size * 56) and (tile_size * 12 <= self.y <= tile_size * 40)) or \
                ((tile_size * 4 <= self.x <= tile_size * 56) and (tile_size * 4 <= self.y <= tile_size * 12)) or \
                ((tile_size * 32 <= self.x <= tile_size * 48) and (tile_size * 33 <= self.y <= tile_size * 40)) or \
                ((tile_size * 32 <= self.x <= tile_size * 40) and (tile_size * 17 <= self.y <= tile_size * 33)) or \
                ((tile_size * 12 <= self.x <= 31 * 32) and (tile_size * 17 <= self.y <= tile_size * 25)) or \
                ((tile_size * 4 <= self.x <= 31 * 12) and (tile_size * 17 <= self.y <= tile_size * 56)) or \
                ((tile_size * 12 <= self.x <= 31 * 48) and (tile_size * 48 <= self.y <= tile_size * 56)):
            #print("road")
            for game_object in game_world.all_objects():
                #print(game_object.__class__.__name__)
                #옵저버와 충돌
                if game_object.__class__.__name__ == 'Observer':
                    #print("sef")
                    if game_object != self:
                        #옵저버가 시작지역 / 안전지역 / 종료지역에 있으면
                        if ((tile_size * 4 <= game_object.x <= tile_size * 12) and (tile_size * 4 <= game_object.y <= tile_size * 12)) or \
                            ((tile_size * 4 <= game_object.x <= tile_size * 12) and (tile_size * 17 <= game_object.y <= tile_size * 25)) or \
                            ((tile_size * 48 <= game_object.x <= tile_size * 56) and (tile_size * 48 <= game_object.y <= tile_size * 56)):
                            pass
                        elif (abs(game_object.x - self.x)<=(game_object.width/2 + self.width/2)) and (abs(game_object.y - self.y)<=(game_object.height/2 + self.height/2)):
                            self.x = 200
                            self.y = 250
                            self.to_x = self.x
                            self.to_y = self.y
                            self.x_velocity = 0
                            self.y_velocity = 0
                            self.curr_t = 0.0
                            self.to_t = 0.0
                            game_world.reset_screen_xy()
        #길 밖으로 나가면
        else:
            self.x = 200
            self.y = 250
            self.to_x = self.x
            self.to_y = self.y
            self.x_velocity = 0
            self.y_velocity = 0
            self.curr_t = 0.0
            self.to_t = 0.0
            game_world.reset_screen_xy()


class Observer(Unit):
    image = None
    width = 36
    height = 34
    max_frame = 28
    ACTION_PER_TIME = 0.5
    velocity = 100.0

    def __init__(self,x,y):
        super(Observer, self).__init__(x, y)


        if Observer.image == None:
            Observer.image = [load_image('resources\\Observer\\%d%d.png' % (i // 10, i % 10)) for i in range(0, 15)]

    def get_events(self):
        pass

    def update(self):
        super(Observer, self).update()



    def draw(self):
        if 15 <= self.frame.current_frame:
            Observer.image[(int)(28- self.frame.current_frame)].composite_draw(3.141595653589793238,'v', self.x - game_world.screen_coord_x, self.y - game_world.screen_coord_y, self.width, self.height)
        else:
            Observer.image[(int)(self.frame.current_frame)].draw(self.x - game_world.screen_coord_x, self.y - game_world.screen_coord_y)


    def set_random_move_point(self):
        super(Observer, self).set_random_move_point()


    def set_move_point(self, to_x, to_y):
        super(Observer, self).set_move_point(to_x, to_y)


    def move(self):
        super(Observer, self).move()

    def set_velocity(self, x_move_distance, y_move_distance):
        super(Observer, self).set_velocity( x_move_distance, y_move_distance)

    def collision_check(self):
        super(Observer, self).collision_check()


class Wraith(Unit):
    image = None
    width = 52
    height = 44
    max_frame = 32
    ACTION_PER_TIME = 0.5
    velocity = 200.0

    def __init__(self, x, y):
        super(Wraith, self).__init__(x, y)

        if Wraith.image == None:
            Wraith.image = [load_image('resources\\Wraith\\%d%d.png' % (i // 10, i % 10)) for i in range(0, 17)]

    def get_events(self):
        pass

    def update(self):
        super(Wraith, self).update()



    def draw(self):
        if 17 <= self.frame.current_frame:
            Wraith.image[(int)(32 - self.frame.current_frame)].composite_draw(3.141595653589793238, 'v', self.x - game_world.screen_coord_x,
                                                                              self.y - game_world.screen_coord_y, self.width, self.height)
        else:
            Wraith.image[(int)(self.frame.current_frame)].draw(self.x - game_world.screen_coord_x, self.y - game_world.screen_coord_y)
    def set_random_move_point(self):
        super(Wraith, self).set_random_move_point()


    def set_move_point(self, to_x, to_y):
        super(Wraith, self).set_move_point(to_x, to_y)


    def move(self):
        super(Wraith, self).move()

    def set_velocity(self, x_move_distance, y_move_distance):
        super(Wraith, self).set_velocity( x_move_distance, y_move_distance)

    def collision_check(self):
        super(Wraith, self).collision_check()



class Scourge(Unit):
    image = None
    width = 31
    height = 27
    max_frame = 16
    ACTION_PER_TIME = 0.5
    velocity = 200.0

    def __init__(self, x, y):
        super(Scourge, self).__init__(x, y)

        self.IDLE_frame = IMG_class.Frame(4, 2)
        self.IDLE_frame.current_frame = 0

        if Scourge.image == None:
            Scourge.image = load_image('resources\\Scourge\\Scourge.png' )

    def get_events(self):
        pass


    def update(self):
        super(Scourge, self).update()
        self.IDLE_frame.update()


    def draw(self):
        if 9 <= self.frame.current_frame:
            Scourge.image.clip_composite_draw((self.width+3) * (16-(int)(self.frame.current_frame)) + 2, 369 - ((self.height+3)*(int)(self.IDLE_frame.current_frame+1)-1),
                                              self.width, self.height - 2, 3.141595653589793238, 'v', self.x - game_world.screen_coord_x, self.y - game_world.screen_coord_y, self.width, self.height)
        else:
            Scourge.image.clip_draw((self.width+3) * (int)(self.frame.current_frame) + 2, 369 - ((self.height+3)*(int)(self.IDLE_frame.current_frame+1)-1), self.width, self.height - 2, self.x - game_world.screen_coord_x,
                                    self.y - game_world.screen_coord_y)


    def set_random_move_point(self):
        super(Scourge, self).set_random_move_point()


    def set_move_point(self, to_x, to_y):
        super(Scourge, self).set_move_point(to_x, to_y)


    def move(self):
        super(Scourge, self).move()

    def set_velocity(self, x_move_distance, y_move_distance):
        super(Scourge, self).set_velocity( x_move_distance, y_move_distance)

    def collision_check(self):
        super(Scourge, self).collision_check()