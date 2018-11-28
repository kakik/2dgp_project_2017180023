import game_world
from pico2d import *
import Unit_class
import game_framework
import Unit_class

background_image = None
bottom_UI = None

collision_box_on = False
stage_level = None
player = None

def create_enemy_observers(level):
    global player

    for i in range(0,9):
        for j in range(0,9):
            for k in range (0,1 + level):
                # 레벨마다 옵저거 81마리씩 늘어남
                game_world.add_object(Unit_class.Observer(game_world.map_x/9*(j+0.5),game_world.map_y/9*(i+0.5)),1)



def delete_enemy_observers():
    global player

    for game_object in game_world.all_objects():
        if isinstance(game_object, Unit_class.Observer):
            if game_object != player:
                # 적 옵저버를 모두 제거
                game_world.remove_object(game_object)


def proceed_next_stage():
    global stage_level
    global player

    player.return_to_start_point()

    delete_enemy_observers()
    stage_level+=1
    create_enemy_observers(stage_level)

def enter():
    global background_image, bottom_UI
    global stage_level

    background_image = MainBGIMG()
    game_world.add_object(background_image, 0)
    bottom_UI = MainBottomUI()
    game_world.add_object(bottom_UI, 1)

    stage_level = 1
    #초기 셋팅 : 옵저버 162 마리
    create_enemy_observers(stage_level)


def exit():

    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global player
    global collision_box_on
    global bottom_UI

    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_w:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = 1
                elif game_world.screen_scroll_y == -1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_a:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = -1
                elif game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = 1
            elif event.key == SDLK_s:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = -1
                elif game_world.screen_scroll_y == 1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_d:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = 1
                elif game_world.screen_scroll_x == -1:
                    game_world.screen_scroll_x = 0
            elif event.key == SDLK_r:
                if collision_box_on == True:
                    collision_box_on = False
                elif collision_box_on == False:
                    collision_box_on = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = -1
                elif game_world.screen_scroll_y == 1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_a:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = 1
                elif game_world.screen_scroll_x == -1:
                    game_world.screen_scroll_x = 0
            elif event.key == SDLK_s:
                if game_world.screen_scroll_y == 0:
                    game_world.screen_scroll_y = 1
                elif game_world.screen_scroll_y == -1:
                    game_world.screen_scroll_y = 0
            elif event.key == SDLK_d:
                if game_world.screen_scroll_x == 0:
                    game_world.screen_scroll_x = -1
                elif game_world.screen_scroll_x == 1:
                    game_world.screen_scroll_x = 0


        if event.type == SDL_MOUSEMOTION:
                # 마우스 좌표 업데이트
                game_world.update_mouse_point(event.x, event.y)

        if event.type == SDL_MOUSEBUTTONDOWN:
            # bottom ui 충돌체크
            bottom_UI_collision_check_result = bottom_UI.collision_check(event.x, event.y)

            #미니맵
            if bottom_UI_collision_check_result == 1:
                pass
            #UI
            elif bottom_UI_collision_check_result == 2:
                pass
            else:
                game_world.cursor.get_events()
                player.get_events()





def update():
    game_world.update_screen_xy()
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    global collision_box_on
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    if collision_box_on == True:
        draw_collision_box()
    update_canvas()


def draw_collision_box():
    # collision boxes for collision_check
    draw_rectangle(31 * 4 - game_world.screen_coord_x, 31 * 4 - game_world.screen_coord_y,
                   31 * 12 - game_world.screen_coord_x, 31 * 12 - game_world.screen_coord_y)
    draw_rectangle(31 * 4 - game_world.screen_coord_x, 31 * 17 - game_world.screen_coord_y,
                   31 * 12 - game_world.screen_coord_x, 31 * 25 - game_world.screen_coord_y)
    draw_rectangle(31 * 48 - game_world.screen_coord_x, 31 * 48 - game_world.screen_coord_y,
                   31 * 56 - game_world.screen_coord_x, 31 * 56 - game_world.screen_coord_y)
    draw_rectangle(31 * 4 - game_world.screen_coord_x, 31 * 4 - game_world.screen_coord_y,
                   31 * 56 - game_world.screen_coord_x, 31 * 12 - game_world.screen_coord_y)
    draw_rectangle(31 * 48 - game_world.screen_coord_x, 31 * 12 - game_world.screen_coord_y,
                   31 * 56 - game_world.screen_coord_x, 31 * 40 - game_world.screen_coord_y)
    draw_rectangle(31 * 32 - game_world.screen_coord_x, 31 * 33 - game_world.screen_coord_y,
                   31 * 48 - game_world.screen_coord_x, 31 * 40 - game_world.screen_coord_y)
    draw_rectangle(31 * 32 - game_world.screen_coord_x, 31 * 17 - game_world.screen_coord_y,
                   31 * 40 - game_world.screen_coord_x, 31 * 33 - game_world.screen_coord_y)
    draw_rectangle(31 * 12 - game_world.screen_coord_x, 31 * 17 - game_world.screen_coord_y,
                   31 * 32 - game_world.screen_coord_x, 31 * 25 - game_world.screen_coord_y)
    draw_rectangle(31 * 4 - game_world.screen_coord_x, 31 * 17 - game_world.screen_coord_y,
                   31 * 12 - game_world.screen_coord_x, 31 * 56 - game_world.screen_coord_y)
    draw_rectangle(31 * 12 - game_world.screen_coord_x, 31 * 48 - game_world.screen_coord_y,
                   31 * 48 - game_world.screen_coord_x, 31 * 56 - game_world.screen_coord_y)





class MainBGIMG():
    image = None
    width = 1860
    height = 1860

    def __init__(self):
        if self.image == None:
            self.image =load_image('resources\\TileMap\\Map.png')

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.clip_draw(game_world.screen_coord_x, game_world.screen_coord_y, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)




class MainBottomUI():
    image = None
    width = 1280
    height = 330
    minimap_image = None
    minimap_image_width = 1860
    minimap_image_height = 1860

    def __init__(self):
        if self.image == None:
            self.image =load_image('resources\\UI\\bottom_UI.png')
        if self.minimap_image == None:
            self.minimap_image = load_image('resources\\TileMap\\Map.png')
        self.minimap_x =game_world.screen_x*27/self.width
        self.minimap_y = game_world.screen_y*6/self.height
        self.minimap_width = game_world.screen_x*256/self.width
        self.minimap_height = (game_world.screen_x /self.width * self.height)*256/self.height
        print(self.minimap_x)

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        global player
        if self.image != None:
            self.image.clip_draw(0, 0, self.width, self.height, int(game_world.screen_x / 2), int(game_world.screen_x /self.width * self.height/2),
                                 game_world.screen_x, int(game_world.screen_x /self.width * self.height))

        #미니맵 배경
        if self.minimap_image != None:
            self.minimap_image.clip_draw(0,0,self.minimap_image_width, self.minimap_image_height,
                                         int((self.minimap_x+self.minimap_width)/2),int((self.minimap_y+self.minimap_height)/2), int(self.minimap_width), int(self.minimap_height))

        #미니맵 내 유닛
        for game_object in game_world.all_objects():
            if game_object == player:
                draw_green_rectangle(
                    int(self.minimap_x / 2 + game_object.unit.x / self.minimap_image_width * self.minimap_width) - 1,
                    int(self.minimap_y / 2 + game_object.unit.y / self.minimap_image_height * self.minimap_height) - 1,
                    int(self.minimap_x / 2 + game_object.unit.x / self.minimap_image_width * self.minimap_width) + 1,
                    int(self.minimap_y / 2 + game_object.unit.y / self.minimap_image_height * self.minimap_height) + 1)

            elif isinstance(game_object, Unit_class.Observer):
                draw_rectangle(int(self.minimap_x/2 + game_object.x/self.minimap_image_width*self.minimap_width)-1,
                               int(self.minimap_y/2+ game_object.y/self.minimap_image_height*self.minimap_height)-1,
                               int(self.minimap_x/2 + game_object.x/self.minimap_image_width*self.minimap_width)+1,
                               int(self.minimap_y/2+ game_object.y/self.minimap_image_height*self.minimap_height)+1)

        draw_white_rectangle(int(self.minimap_x / 2 + game_world.screen_coord_x / self.minimap_image_width * self.minimap_width) ,
                       int(self.minimap_y / 2 + (game_world.screen_coord_y + self.height/3  )/ self.minimap_image_height * self.minimap_height)  ,
                       int(self.minimap_x / 2 + (game_world.screen_coord_x + game_world.screen_x) / self.minimap_image_width * self.minimap_width) ,
                       int(self.minimap_y / 2 + (game_world.screen_coord_y + game_world.screen_y) / self.minimap_image_height * self.minimap_height) )


        #draw_rectangle(self.minimap_x, self.minimap_y, self.minimap_width + self.minimap_x, self.minimap_height + self.minimap_y)

    def collision_check(self, event_x, event_y):
        global is_scrolling_screen
        event_y = (game_world.screen_y - event_y - 1)

        #바텀 UI 충돌체크
        if (self.minimap_x < event_x < self.minimap_x + self.minimap_width and self.minimap_y < event_y < self.minimap_y + self.minimap_height):
            return 1 #미니맵
        elif (0 < event_x < (330 * game_world.screen_x / self.width) and 0 < event_y < (game_world.screen_x / self.width * self.height) or
              (330 * game_world.screen_x / self.width) < event_x <  game_world.screen_x - (310 * game_world.screen_x / self.width)  and 0 < event_y < (game_world.screen_x / self.width * 225) or
                game_world.screen_x - (310 * game_world.screen_x / self.width) < event_x < game_world.screen_x and 0 < event_y < game_world.screen_x / self.width * 350 ):
            return 2 #UI
        else:
            return 3













