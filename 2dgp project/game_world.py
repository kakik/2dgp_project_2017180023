import game_framework
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for o in all_objects():
        del o
    objects.clear()


def all_objects():
    global cursor
    global mx, my
    is_curror_exist = False

    for i in range(len(objects)):
        for o in objects[i]:
            #커서 맨 위로
            if o == cursor:
                is_curror_exist = True
                continue
            yield o

    if is_curror_exist == True:
        yield cursor




# 마우스 좌표
mx, my = None, None

def update_mouse_point(x, y):
    global mx, my
    global screen_x, screen_y
    global screen_coord_x, screen_coord_y

    mx = x + screen_coord_x
    my = screen_y - y + screen_coord_y

cursor = None

#스크린 좌하단 좌표
screen_coord_x, screen_coord_y = 0, 0
screen_coordf_x, screen_coordf_y = 0, 0
screen_scroll_x, screen_scroll_y = 0,0
screen_scroll_speed = 400
def update_screen_xy():
    global screen_coord_x, screen_coord_y, screen_scroll_x, screen_scroll_y ,screen_scroll_speed, screen_coordf_x, screen_coordf_y
    global map_x, map_y
    global screen_coord_x, screen_coord_y
    global mx, my

    if 0<= screen_coordf_x +screen_scroll_speed * screen_scroll_x * game_framework.frame_time<= map_x - screen_x:
        screen_coordf_x = (screen_coordf_x + screen_scroll_speed * screen_scroll_x* game_framework.frame_time)%(map_x - screen_x)
        mx = ( mx + screen_scroll_speed * screen_scroll_x* game_framework.frame_time)%map_x


    if 0 <= screen_coordf_y + screen_scroll_speed * screen_scroll_y * game_framework.frame_time <= map_y - screen_y:
        screen_coordf_y = (screen_coordf_y + screen_scroll_speed * screen_scroll_y * game_framework.frame_time)%(map_y - screen_y)
        my =( my + screen_scroll_speed * screen_scroll_y * game_framework.frame_time)%map_y

    screen_coord_x = (int)(screen_coordf_x)
    screen_coord_y = (int)(screen_coordf_y)

def reset_screen_xy():
    global screen_coordf_x, screen_coordf_y

    screen_coordf_x, screen_coordf_y =0,0



#맵 사이즈
map_x, map_y = 1860, 1860

#스크린 사이즈
screen_x, screen_y = 800,600