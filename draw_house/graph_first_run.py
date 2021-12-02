from graph.graph import *


def keyPressed(event):
    moveObjectBy(obj1, -5, 0)


obj1 = rectangle(300, 300, 350, 400)

onKey('Left', keyPressed)

run()


# import tkinter as tk
# def __keyPress(event):
#   print("Key Press Event:")
#   print("  event.char:", event.char)
#   print("  event.keysym:", event.keysym)
#   print("  event.keycode:", event.keycode)
#   print("  event.keysym_num:", event.keysym_num)
# root = tk.Tk()
# root.bind("<KeyPress>", __keyPress)
# tk.mainloop()
