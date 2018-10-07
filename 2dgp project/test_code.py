from pico2d import *
from tkinter import *
from enum import Enum
import threading
import random

import math

Window_Width = 1600
Window_Height = 900
i='aaaaaaaa'

current_window = 0  # 0 = 스타트 화면 1 = 인게임 화면
is_window_looping = False
window = Tk()

bg_img = PhotoImage(file="kakiku.png")
game_main_background = Label(window, image=bg_img)

canvas=Canvas(window, relief="solid", bd=2)

def movesaf(event):
    global window
    global i
    global canvas

    game_main_background.place(x=event.x, y=event.y, width=100, height=500)
    canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="red", width=10)

def set_window():
    global current_window
    global window


    if current_window == 0:
        window.title("test 1")
        window.geometry("1600x900+100+100")
        window.resizable(False, False)


        main_screen = Label(window, width=Window_Width, height=Window_Height,state='active',activebackground='white')
        main_screen.place(x=0, y=0)
        main_screen.bind("<B1-Motion>", movesaf)

        game_title = Label(window, width=100, height=100, text=i)
        game_title.place(x=600,y=300,width=100,height=50)
        game_title.bind("<B1-Motion>", movesaf)

        canvas.pack(expand=True, fill="both")

    elif current_window == 1:
        pass

    window.mainloop()


class Scourage:
    def __init__(self):
        self.x = random.randint(10, 800 - 10)
        self.y = random.randint(10, 400 - 10)
        self.to_x = random.randint(10, 800 - 10)
        self.to_y = random.randint(10, 400 - 10)
        self.speed = 5
        self.in_move_delay = True
        self.delay_time = 0


def start_setting():
    global current_window

    current_window = 0


def move_scourages():
    pass


def draw_background():
    clear_canvas()
    background.clip_draw(0, 0, Canvas_Width, Canvas_Height, 0, 0)
    update_canvas()


start_setting()


set_window()
