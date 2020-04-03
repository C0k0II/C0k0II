from Tkinter import *

root = Tk()


def key(event):
    print ('pressed', repr(event.char)


def d(event):
    print ('clicked at', event.x, event.y)



frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", d)
frame.pack()

root.mainloop()
