from tkinter import *
from time import *

def handler1(event):
    """Главный цикл игры"""
    global x, y
    print( event.x, event.y)
    if (event.x in range(243,594)) and (event.y in range(209,265)):
        print('Begin')
        game_menu_main.grid_remove()
        game_start()

    elif (event.x in range(285,534)) and (event.y in range(301,356)):
        print('Settings')
        game_menu_main.destroy()

    elif (event.x in range(343,473)) and (event.y in range(392,443)):
        exit()

def handler2(event):
    #Возвращает код клавиши
    global x, y, speed
    if event.keycode==87:
        y-=speed

    elif event.keycode==83:
        y+=speed

    elif event.keycode==65:
        x-=speed

    elif event.keycode==68:
        x+=speed

    root.after(33,game_start)


def game_start():
    """Создание нового героя"""
    hero=Label(root, image=hero_img)
    hero.place(x=x,y=y)

    root.bind('<Key>',handler2)

root=Tk()
x=10
y=10
speed=20

Main_menu=""" Start Game
Settings
Exit
"""
exiit=False
#init main menu
main_background=PhotoImage(file="main.png")
hero_img=PhotoImage(file="hero.png")


game_menu_main=Label(root, text=Main_menu, font='Times 60', width=810, height=810, image=main_background,fg='#fa9600',compound='center')
game_menu_main.grid()

# connect with event
game_menu_main.bind('<Button-1>',handler1)



root.mainloop()
