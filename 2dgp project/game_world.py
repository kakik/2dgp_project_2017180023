import cursor_class
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
            return


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
    mx = x
    my = 600 - y

cursor = None

#스크린 좌하단 좌표
screen_x, screen_y = 0,0

#맵 사이즈
map_x, map_y = 1860, 1860

#스크린 사이즈